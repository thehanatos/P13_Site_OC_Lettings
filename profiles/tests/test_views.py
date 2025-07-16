import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_index_view(client):
    user = User.objects.create(username="alice")
    Profile.objects.create(user=user, favorite_city="Lyon")
    response = client.get(reverse('profiles:index'))
    assert response.status_code == 200
    assert b"alice" in response.content
