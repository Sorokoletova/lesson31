import pytest
from tests.factories import AdsFactory


@pytest.mark.django_db
def test_ads_create(client, user):
    ads = AdsFactory.create()

    response = client.post(
        "/ad/create/",
        {
            "name": "test name",
            "author": 1,
            "price": 1500,
            "description": "description test",
            "is_published": False,
            "category": 1
        },
        content_type="application/json",
    )
    expected_response = {
        "name": "test name",
        "author": 1,
        "price": 1500,
        "description": "description test",
        "is_published": False,
        "image": ads.image.url if ads.image else None,
        "category": 1

    }

    assert response.status_code == 201
    assert response.data == expected_response
