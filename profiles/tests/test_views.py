import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_detail_view(client):
    user = User.objects.create(username="bob")
    profile = Profile.objects.create(user=user, favorite_city="Tokyo")

    url = reverse('profiles:profile', kwargs={'username': user.username})
    response = client.get(url)

    assert response.status_code == 200
    assert b"bob" in response.content
    assert profile.favorite_city.encode() in response.content
