from datetime import date, timedelta


def should_create_task_and_return_201(client):
    response = client.post('/tasks/', json={'title': 'Write tests'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Write tests'
    assert data['status'] == 'todo'
    assert data['priority'] == 'medium'
    assert 'id' in data
    assert 'created_at' in data
    assert 'tags' in data
    assert data['is_overdue'] is False


def should_create_task_with_project_id(client):
    project_resp = client.post('/projects/', json={'name': 'My Project'})
    project_id = project_resp.get_json()['id']

    response = client.post('/tasks/', json={'title': 'Task in project', 'project_id': project_id})
    assert response.status_code == 201
    data = response.get_json()
    assert data['project_id'] == project_id


def should_return_404_when_project_id_does_not_exist(client):
    response = client.post('/tasks/', json={'title': 'Ghost task', 'project_id': 99999})
    assert response.status_code == 404


def should_return_422_when_title_is_empty_string(client):
    response = client.post('/tasks/', json={'title': ''})
    assert response.status_code == 422


def should_return_422_when_status_is_invalid(client):
    response = client.post('/tasks/', json={'title': 'x', 'status': 'flying'})
    assert response.status_code == 422


def should_return_422_when_priority_is_invalid(client):
    response = client.post('/tasks/', json={'title': 'x', 'priority': 'critical'})
    assert response.status_code == 422


def should_return_empty_list_when_no_tasks_exist(client):
    response = client.get('/tasks/')
    assert response.status_code == 200
    assert response.get_json() == []


def should_list_all_tasks(client):
    client.post('/tasks/', json={'title': 'Task One'})
    client.post('/tasks/', json={'title': 'Task Two'})
    response = client.get('/tasks/')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    titles = [t['title'] for t in data]
    assert 'Task One' in titles
    assert 'Task Two' in titles


def should_filter_tasks_by_project_id(client):
    project_resp = client.post('/projects/', json={'name': 'Project Alpha'})
    project_id = project_resp.get_json()['id']

    client.post('/tasks/', json={'title': 'In project', 'project_id': project_id})
    client.post('/tasks/', json={'title': 'No project'})

    response = client.get(f'/tasks/?project_id={project_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['title'] == 'In project'


def should_filter_tasks_by_status(client):
    client.post('/tasks/', json={'title': 'Todo task', 'status': 'todo'})
    client.post('/tasks/', json={'title': 'Done task', 'status': 'done'})

    response = client.get('/tasks/?status=todo')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['title'] == 'Todo task'


def should_return_422_when_status_filter_is_invalid(client):
    response = client.get('/tasks/?status=nonsense')
    assert response.status_code == 422


def should_filter_tasks_by_project_id_and_status(client):
    project_resp = client.post('/projects/', json={'name': 'Project Beta'})
    project_id = project_resp.get_json()['id']

    client.post('/tasks/', json={'title': 'In project todo', 'project_id': project_id, 'status': 'todo'})
    client.post('/tasks/', json={'title': 'In project done', 'project_id': project_id, 'status': 'done'})
    client.post('/tasks/', json={'title': 'Other project todo', 'status': 'todo'})

    response = client.get(f'/tasks/?project_id={project_id}&status=todo')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['title'] == 'In project todo'


def should_get_task_by_id(client):
    create_resp = client.post('/tasks/', json={'title': 'Find me'})
    task_id = create_resp.get_json()['id']

    response = client.get(f'/tasks/{task_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == task_id
    assert data['title'] == 'Find me'
    assert 'tags' in data


def should_return_404_when_task_not_found(client):
    response = client.get('/tasks/99999')
    assert response.status_code == 404


def should_update_task_title(client):
    create_resp = client.post('/tasks/', json={'title': 'Old Title'})
    task_id = create_resp.get_json()['id']

    response = client.put(f'/tasks/{task_id}', json={'title': 'New Title'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == 'New Title'


def should_clear_description_when_null_is_sent_on_update(client):
    create_resp = client.post('/tasks/', json={'title': 'My Task', 'description': 'Old desc'})
    task_id = create_resp.get_json()['id']

    response = client.put(f'/tasks/{task_id}', json={'description': None})
    assert response.status_code == 200
    assert response.get_json()['description'] is None


def should_update_task_status_to_in_progress(client):
    create_resp = client.post('/tasks/', json={'title': 'Status task'})
    task_id = create_resp.get_json()['id']

    response = client.put(f'/tasks/{task_id}', json={'status': 'in_progress'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'in_progress'


def should_return_404_on_update_when_task_not_found(client):
    response = client.put('/tasks/99999', json={'title': 'Ghost'})
    assert response.status_code == 404


def should_update_task_due_date(client):
    create_resp = client.post('/tasks/', json={'title': 'Due date task'})
    task_id = create_resp.get_json()['id']

    response = client.put(f'/tasks/{task_id}', json={'due_date': '2099-12-31'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['due_date'] == '2099-12-31'
    assert data['is_overdue'] is False


def should_return_422_when_updating_with_blank_title(client):
    create_resp = client.post('/tasks/', json={'title': 'Valid title'})
    task_id = create_resp.get_json()['id']

    response = client.put(f'/tasks/{task_id}', json={'title': ''})
    assert response.status_code == 422


def should_return_422_when_updating_with_invalid_status(client):
    create_resp = client.post('/tasks/', json={'title': 'Status task'})
    task_id = create_resp.get_json()['id']

    response = client.put(f'/tasks/{task_id}', json={'status': 'bogus'})
    assert response.status_code == 422


def should_clear_due_date_via_update(client):
    from datetime import date, timedelta
    past_date = (date.today() - timedelta(days=3)).isoformat()
    create_resp = client.post('/tasks/', json={'title': 'Overdue clear', 'due_date': past_date})
    task_id = create_resp.get_json()['id']
    assert create_resp.get_json()['is_overdue'] is True

    response = client.put(f'/tasks/{task_id}', json={'due_date': None})
    assert response.status_code == 200
    assert response.get_json()['is_overdue'] is False


def should_delete_task_and_return_204(client):
    create_resp = client.post('/tasks/', json={'title': 'Delete me'})
    task_id = create_resp.get_json()['id']

    response = client.delete(f'/tasks/{task_id}')
    assert response.status_code == 204

    get_resp = client.get(f'/tasks/{task_id}')
    assert get_resp.status_code == 404


def should_return_404_on_delete_when_task_not_found(client):
    response = client.delete('/tasks/99999')
    assert response.status_code == 404


def should_attach_tag_to_task_and_return_200(client):
    tag_resp = client.post('/tags/', json={'name': 'critical', 'color': '#FF0000'})
    tag_id = tag_resp.get_json()['id']

    task_resp = client.post('/tasks/', json={'title': 'Tagged task'})
    task_id = task_resp.get_json()['id']

    response = client.post(f'/tasks/{task_id}/tags/{tag_id}')
    assert response.status_code == 200
    data = response.get_json()
    tag_names = [t['name'] for t in data['tags']]
    assert 'critical' in tag_names


def should_return_404_when_attaching_tag_to_nonexistent_task(client):
    tag_resp = client.post('/tags/', json={'name': 'some-tag', 'color': '#000000'})
    tag_id = tag_resp.get_json()['id']

    response = client.post(f'/tasks/99999/tags/{tag_id}')
    assert response.status_code == 404


def should_be_idempotent_when_attaching_already_attached_tag(client):
    tag_resp = client.post('/tags/', json={'name': 'idempotent-tag', 'color': '#CCCCCC'})
    tag_id = tag_resp.get_json()['id']

    task_resp = client.post('/tasks/', json={'title': 'Idempotent task'})
    task_id = task_resp.get_json()['id']

    client.post(f'/tasks/{task_id}/tags/{tag_id}')
    response = client.post(f'/tasks/{task_id}/tags/{tag_id}')

    assert response.status_code == 200
    assert len(response.get_json()['tags']) == 1


def should_return_404_when_attaching_nonexistent_tag_to_task(client):
    task_resp = client.post('/tasks/', json={'title': 'Some task'})
    task_id = task_resp.get_json()['id']

    response = client.post(f'/tasks/{task_id}/tags/99999')
    assert response.status_code == 404


def should_detach_tag_from_task_and_return_204(client):
    tag_resp = client.post('/tags/', json={'name': 'removable', 'color': '#AAAAAA'})
    tag_id = tag_resp.get_json()['id']

    task_resp = client.post('/tasks/', json={'title': 'Task with tag'})
    task_id = task_resp.get_json()['id']

    client.post(f'/tasks/{task_id}/tags/{tag_id}')

    response = client.delete(f'/tasks/{task_id}/tags/{tag_id}')
    assert response.status_code == 204

    get_resp = client.get(f'/tasks/{task_id}')
    tag_names = [t['name'] for t in get_resp.get_json()['tags']]
    assert 'removable' not in tag_names


def should_return_404_when_detaching_tag_not_attached_to_task(client):
    tag_resp = client.post('/tags/', json={'name': 'not-attached', 'color': '#DDDDDD'})
    tag_id = tag_resp.get_json()['id']

    task_resp = client.post('/tasks/', json={'title': 'Task without tag'})
    task_id = task_resp.get_json()['id']

    response = client.delete(f'/tasks/{task_id}/tags/{tag_id}')
    assert response.status_code == 404


def should_return_404_when_detaching_tag_from_nonexistent_task(client):
    tag_resp = client.post('/tags/', json={'name': 'orphan-tag', 'color': '#BBBBBB'})
    tag_id = tag_resp.get_json()['id']

    response = client.delete(f'/tasks/99999/tags/{tag_id}')
    assert response.status_code == 404


def should_include_tags_in_task_response(client):
    tag_resp = client.post('/tags/', json={'name': 'visible', 'color': '#123456'})
    tag_id = tag_resp.get_json()['id']

    task_resp = client.post('/tasks/', json={'title': 'Task showing tags'})
    task_id = task_resp.get_json()['id']

    client.post(f'/tasks/{task_id}/tags/{tag_id}')

    response = client.get(f'/tasks/{task_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['tags']) == 1
    assert data['tags'][0]['name'] == 'visible'


def should_return_is_overdue_false_after_marking_overdue_task_done(client):
    from datetime import date, timedelta
    past_date = (date.today() - timedelta(days=2)).isoformat()
    create_resp = client.post('/tasks/', json={'title': 'Mark done', 'due_date': past_date})
    task_id = create_resp.get_json()['id']
    assert create_resp.get_json()['is_overdue'] is True

    response = client.put(f'/tasks/{task_id}', json={'status': 'done'})
    assert response.status_code == 200
    assert response.get_json()['is_overdue'] is False


def should_return_is_overdue_true_when_due_date_is_past_and_not_done(client):
    past_date = (date.today() - timedelta(days=3)).isoformat()
    response = client.post('/tasks/', json={'title': 'Overdue task', 'due_date': past_date, 'status': 'todo'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['is_overdue'] is True
