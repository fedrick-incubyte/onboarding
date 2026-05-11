"""Integration tests for the projects routes."""


def should_return_401_when_creating_project_without_auth(client):
    response = client.post("/projects/", json={"name": "Work"})
    assert response.status_code == 401


def should_return_201_when_creating_project_with_auth(client, register_and_login):
    token = register_and_login()
    response = client.post("/projects/", json={"name": "Work"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 201
    assert response.get_json()["name"] == "Work"


def should_only_return_projects_belonging_to_current_user(client, register_and_login):
    token_a = register_and_login("a@example.com")
    token_b = register_and_login("b@example.com")
    client.post("/projects/", json={"name": "A's project"}, headers={"Authorization": f"Bearer {token_a}"})
    client.post("/projects/", json={"name": "B's project"}, headers={"Authorization": f"Bearer {token_b}"})
    data = client.get("/projects/", headers={"Authorization": f"Bearer {token_a}"}).get_json()
    assert len(data) == 1 and data[0]["name"] == "A's project"


def should_return_404_when_accessing_another_users_project(client, register_and_login):
    token_a = register_and_login("a@example.com")
    token_b = register_and_login("b@example.com")
    pid = client.post("/projects/", json={"name": "Private"}, headers={"Authorization": f"Bearer {token_a}"}).get_json()["id"]
    response = client.get(f"/projects/{pid}", headers={"Authorization": f"Bearer {token_b}"})
    assert response.status_code == 404


def should_return_200_when_accessing_own_project(client, register_and_login):
    token = register_and_login()
    pid = client.post("/projects/", json={"name": "Mine"}, headers={"Authorization": f"Bearer {token}"}).get_json()["id"]
    response = client.get(f"/projects/{pid}", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.get_json()["name"] == "Mine"


def should_return_200_when_updating_project_name(client, register_and_login):
    token = register_and_login()
    headers = {"Authorization": f"Bearer {token}"}
    pid = client.post("/projects/", json={"name": "Old Name"}, headers=headers).get_json()["id"]
    response = client.put(f"/projects/{pid}", json={"name": "New Name"}, headers=headers)
    assert response.status_code == 200
    assert response.get_json()["name"] == "New Name"


def should_return_204_when_deleting_project(client, register_and_login):
    token = register_and_login()
    headers = {"Authorization": f"Bearer {token}"}
    pid = client.post("/projects/", json={"name": "Temp"}, headers=headers).get_json()["id"]
    response = client.delete(f"/projects/{pid}", headers=headers)
    assert response.status_code == 204
