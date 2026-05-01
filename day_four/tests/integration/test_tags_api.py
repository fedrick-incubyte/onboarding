def should_create_tag_and_return_201(client):
    response = client.post('/tags/', json={'name': 'urgent', 'color': '#FF0000'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'urgent'
    assert data['color'] == '#FF0000'
    assert 'id' in data


def should_return_empty_list_when_no_tags_exist(client):
    response = client.get('/tags/')
    assert response.status_code == 200
    assert response.get_json() == []


def should_list_all_tags(client):
    client.post('/tags/', json={'name': 'bug', 'color': '#FF0000'})
    client.post('/tags/', json={'name': 'feature', 'color': '#00FF00'})
    response = client.get('/tags/')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    names = [t['name'] for t in data]
    assert 'bug' in names
    assert 'feature' in names


def should_delete_tag_and_return_204(client):
    create_resp = client.post('/tags/', json={'name': 'to-delete', 'color': '#000000'})
    tag_id = create_resp.get_json()['id']

    response = client.delete(f'/tags/{tag_id}')
    assert response.status_code == 204

    list_resp = client.get('/tags/')
    names = [t['name'] for t in list_resp.get_json()]
    assert 'to-delete' not in names


def should_return_404_on_delete_when_tag_not_found(client):
    response = client.delete('/tags/99999')
    assert response.status_code == 404


def should_return_422_when_name_missing_on_create(client):
    response = client.post('/tags/', json={'color': '#FF0000'})
    assert response.status_code == 422


def should_return_422_when_color_missing_on_create(client):
    response = client.post('/tags/', json={'name': 'no-color'})
    assert response.status_code == 422


def should_return_422_when_color_is_not_valid_hex(client):
    response = client.post('/tags/', json={'name': 'bad-color', 'color': 'notacolor'})
    assert response.status_code == 422


def should_return_409_when_tag_name_already_exists(client):
    client.post('/tags/', json={'name': 'duplicate', 'color': '#AAAAAA'})
    response = client.post('/tags/', json={'name': 'duplicate', 'color': '#BBBBBB'})
    assert response.status_code == 409


def should_remove_tag_from_task_when_tag_is_deleted(client):
    tag_resp = client.post('/tags/', json={'name': 'cascade-tag', 'color': '#111111'})
    tag_id = tag_resp.get_json()['id']

    task_resp = client.post('/tasks/', json={'title': 'Task with cascade tag'})
    task_id = task_resp.get_json()['id']

    client.post(f'/tasks/{task_id}/tags/{tag_id}')

    client.delete(f'/tags/{tag_id}')

    get_resp = client.get(f'/tasks/{task_id}')
    assert get_resp.status_code == 200
    assert get_resp.get_json()['tags'] == []
