def test_characters(client):
    response = client.get(f"/characters/{2}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Morty Smith"
    assert data["status"] == "Alive"
    assert data["species"] == "Human"
