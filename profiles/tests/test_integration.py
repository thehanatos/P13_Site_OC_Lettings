import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_index_displays_user_and_favorite_city(client):
    user = User.objects.create(username="caroline")
    Profile.objects.create(user=user, favorite_city="Tokyo")

    url = reverse("profiles:index")
    response = client.get(url)

    assert response.status_code == 200
    assert b"caroline" in response.content
    assert b"Tokyo" in response.content
