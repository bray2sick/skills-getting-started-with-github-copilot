def test_get_activities_returns_expected_payload(client):
    # Arrange
    expected_keys = {
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Soccer Team",
        "Basketball Club",
        "Art Studio",
        "Drama Club",
        "Debate Team",
        "Math Olympiad",
    }

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert set(payload.keys()) == expected_keys

    for activity_data in payload.values():
        assert "description" in activity_data
        assert isinstance(activity_data["description"], str)
        assert "schedule" in activity_data
        assert isinstance(activity_data["schedule"], str)
        assert "max_participants" in activity_data
        assert isinstance(activity_data["max_participants"], int)
        assert "participants" in activity_data
        assert isinstance(activity_data["participants"], list)


def test_root_redirects_to_static_index(client):
    # Arrange
    route = "/"

    # Act
    response = client.get(route, follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"
