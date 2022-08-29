import pytest
from tests.factories import AdsFactory


@pytest.mark.django_db
def test_ads_create(client, categorie, user):
    ads = AdsFactory.create()

    response = client.post(
        "/ad/create/",
        {
            "name": "test names",
            "author": user.id,
            "price": 1500,
            "description": "description test",
            "is_published": False,
            "category": categorie.id,
        },
        content_type="application/json",
    )
    expected_response = {
        "id": 2,
        "name": "test names",
        "author": user.id,
        "price": 1500,
        "description": "description test",
        "is_published": False,
        "category": categorie.id,
    }

    assert response.status_code == 201
    assert response.data == expected_response
