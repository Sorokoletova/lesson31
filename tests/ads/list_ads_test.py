import pytest
from tests.factories import AdsFactory


@pytest.mark.django_db
def test_ads_list(client):
    ads_factory = AdsFactory.create_batch(5)

    response = client.get("/ad/")
    ads = []
    for ad in ads_factory:
        ads.append(
            {
                "id": ad.id,
                "name": ad.name,
                "author": ad.author.username,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "category": ad.category.name,
                "image": ad.image.url if ad.image else None,
            }
        )

    expected_response = {
        "count": 5,
        "next": None,
        "previous": None,
        "results": ads
    }
    assert response.status_code == 200
    assert response.json() == expected_response
