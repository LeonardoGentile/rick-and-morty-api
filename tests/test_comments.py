def test_comment(client):
    # Add comment to episode
    response = client.post("/comments", json={"content": "Tiny Rick!!", "episode_id": 2, "character_id": 0})
    assert response.status_code == 201
    response = client.get(f"/comments/{1}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["content"] == "Tiny Rick!!"
    assert data["episode_id"] == 2

