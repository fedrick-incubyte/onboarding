"""End-to-end smoke tests for the full user journey."""


def should_complete_full_user_journey(client, register_and_login):
    token = register_and_login()
    headers = {"Authorization": f"Bearer {token}"}
    proj_id = client.post("/projects/", json={"name": "My Project"}, headers=headers).get_json()["id"]
    task_id = client.post("/tasks/", json={"title": "First Task", "project_id": proj_id}, headers=headers).get_json()["id"]
    assert len(client.get("/tasks/", headers=headers).get_json()) == 1
    client.delete(f"/tasks/{task_id}", headers=headers)
    assert client.get(f"/tasks/{task_id}", headers=headers).status_code == 404


def should_enforce_data_isolation_between_two_users(client, register_and_login):
    token_alice = register_and_login("alice@example.com")
    token_bob = register_and_login("bob@example.com")
    client.post("/projects/", json={"name": "Alice's"}, headers={"Authorization": f"Bearer {token_alice}"})
    client.post("/projects/", json={"name": "Bob's"}, headers={"Authorization": f"Bearer {token_bob}"})
    alice_projects = client.get("/projects/", headers={"Authorization": f"Bearer {token_alice}"}).get_json()
    bob_projects = client.get("/projects/", headers={"Authorization": f"Bearer {token_bob}"}).get_json()
    assert len(alice_projects) == 1 and alice_projects[0]["name"] == "Alice's"
    assert len(bob_projects) == 1 and bob_projects[0]["name"] == "Bob's"
