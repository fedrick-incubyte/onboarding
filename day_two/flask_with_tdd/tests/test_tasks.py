def test_get_tasks_returns_empty_list(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert response.get_json() == []


def test_create_task(client):
    response = client.post('/tasks', json={'title': 'Buy milk'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Buy milk'
    assert 'id' in data


def test_get_tasks_shows_created_task(client):
    client.post('/tasks', json={'title': 'Read a book'})
    response = client.get('/tasks')
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['title'] == 'Read a book'


def test_get_single_task(client):
    post_resp = client.post('/tasks', json={'title': 'Write tests'})
    task_id = post_resp.get_json()['id']
    response = client.get(f'/tasks/{task_id}')
    assert response.status_code == 200
    assert response.get_json()['title'] == 'Write tests'


def test_get_nonexistent_task_returns_404(client):
    response = client.get('/tasks/does-not-exist')
    assert response.status_code == 404


def test_update_task(client):
    post_resp = client.post('/tasks', json={'title': 'Old title'})
    task_id = post_resp.get_json()['id']
    response = client.put(f'/tasks/{task_id}', json={'title': 'New title', 'done': True})
    assert response.status_code == 200
    assert response.get_json()['title'] == 'New title'
    assert response.get_json()['done'] is True


def test_delete_task(client):
    post_resp = client.post('/tasks', json={'title': 'Temporary'})
    task_id = post_resp.get_json()['id']
    assert client.delete(f'/tasks/{task_id}').status_code == 204
    assert client.get(f'/tasks/{task_id}').status_code == 404


def test_create_task_without_title_returns_400(client):
    response = client.post('/tasks', json={})
    assert response.status_code == 400
    assert 'error' in response.get_json()
