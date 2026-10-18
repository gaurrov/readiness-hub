def test_rejects_empty_name(client):
    response = client.post("/students", json={"name": ""})
    assert response.status_code == 400
    assert response.get_json()["error"] == "Name is required"
