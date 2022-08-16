import pytest
from ads.serializers import AdsSerializer
@pytest.mark.django_db
def test_ad_detail(client, ads, user_token):
    response = client.get(
        f'/ad/{ads.id}/',
        content_type='application/json',
        HTTP_AUTHORIZATION=f'Bearer {user_token}'
    )
    assert response.status_code == 200
    assert response.data == AdsSerializer(ads).data