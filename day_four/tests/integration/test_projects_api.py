def should_create_project_and_return_201(client):
    response = client.post('/projects/', json={'name': 'Alpha Project', 'description': 'First project'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Alpha Project'
    assert data['description'] == 'First project'
    assert 'id' in data
    assert 'created_at' in data


def should_return_empty_list_when_no_projects_exist(client):
    response = client.get('/projects/')
    assert response.status_code == 200
    assert response.get_json() == []


def should_list_all_projects(client):
    client.post('/projects/', json={'name': 'Project A'})
    client.post('/projects/', json={'name': 'Project B'})
    response = client.get('/projects/')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    names = [p['name'] for p in data]
    assert 'Project A' in names
    assert 'Project B' in names


def should_return_404_when_project_not_found(client):
    response = client.get('/projects/99999')
    assert response.status_code == 404


def should_update_project_name(client):
    create_resp = client.post('/projects/', json={'name': 'Old Name'})
    project_id = create_resp.get_json()['id']

    response = client.put(f'/projects/{project_id}', json={'name': 'New Name'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'New Name'


def should_return_404_on_update_when_project_not_found(client):
    response = client.put('/projects/99999', json={'name': 'Whatever'})
    assert response.status_code == 404


def should_delete_project_and_return_204(client):
    create_resp = client.post('/projects/', json={'name': 'To Be Deleted'})
    project_id = create_resp.get_json()['id']

    response = client.delete(f'/projects/{project_id}')
    assert response.status_code == 204

    get_resp = client.get(f'/projects/{project_id}')
    assert get_resp.status_code == 404


def should_return_404_on_delete_when_project_not_found(client):
    response = client.delete('/projects/99999')
    assert response.status_code == 404


def should_return_422_when_name_missing_on_create(client):
    response = client.post('/projects/', json={'description': 'No name here'})
    assert response.status_code == 422


def should_return_422_when_name_is_empty_string(client):
    response = client.post('/projects/', json={'name': ''})
    assert response.status_code == 422


def should_return_422_when_updating_with_blank_name(client):
    create_resp = client.post('/projects/', json={'name': 'Valid Name'})
    project_id = create_resp.get_json()['id']

    response = client.put(f'/projects/{project_id}', json={'name': ''})
    assert response.status_code == 422


def should_return_422_when_name_exceeds_200_chars(client):
    response = client.post('/projects/', json={'name': 'x' * 201})
    assert response.status_code == 422


def should_clear_description_when_null_is_sent_on_update(client):
    create_resp = client.post('/projects/', json={'name': 'Proj', 'description': 'Old desc'})
    project_id = create_resp.get_json()['id']

    response = client.put(f'/projects/{project_id}', json={'description': None})
    assert response.status_code == 200
    assert response.get_json()['description'] is None


def should_update_only_description_leaving_name_unchanged(client):
    create_resp = client.post('/projects/', json={'name': 'Original Name'})
    project_id = create_resp.get_json()['id']

    response = client.put(f'/projects/{project_id}', json={'description': 'New desc'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Original Name'
    assert data['description'] == 'New desc'


def should_include_nested_tasks_in_project_response(client):
    project_resp = client.post('/projects/', json={'name': 'Nested Tasks Project'})
    project_id = project_resp.get_json()['id']

    client.post('/tasks/', json={'title': 'Task Alpha', 'project_id': project_id})
    client.post('/tasks/', json={'title': 'Task Beta', 'project_id': project_id})

    response = client.get(f'/projects/{project_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['tasks']) == 2
    titles = [t['title'] for t in data['tasks']]
    assert 'Task Alpha' in titles
    assert 'Task Beta' in titles
    assert 'status' in data['tasks'][0]


def should_cascade_delete_tasks_when_project_is_deleted(client):
    project_resp = client.post('/projects/', json={'name': 'Cascade Project'})
    project_id = project_resp.get_json()['id']

    task_resp = client.post('/tasks/', json={'title': 'Orphaned Task', 'project_id': project_id})
    task_id = task_resp.get_json()['id']

    client.delete(f'/projects/{project_id}')

    get_resp = client.get(f'/tasks/{task_id}')
    assert get_resp.status_code == 404


def should_get_project_by_id_with_tasks(client):
    create_resp = client.post('/projects/', json={'name': 'My Project'})
    project_id = create_resp.get_json()['id']

    response = client.get(f'/projects/{project_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == project_id
    assert data['name'] == 'My Project'
    assert 'tasks' in data
    assert isinstance(data['tasks'], list)
