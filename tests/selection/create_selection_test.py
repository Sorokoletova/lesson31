import pytest


@pytest.mark.django_db
def test_selection_create(client, user_token, user, ads):
    response = client.post(
        "/selection/create/",
        {
            "name": "test name",
            "owner": user.id,
            "items": [ads.id]
        },
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {user_token}"
    )

    expected_response = {
        "id": 1,
        "name": "test name",
        "owner": user.id,
        "items": [ads.id]
    }

    assert response.status_code == 201
    assert response.data == expected_response
