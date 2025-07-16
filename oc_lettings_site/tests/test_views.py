import pytest
from django.urls import reverse
from django.http import HttpRequest
from oc_lettings_site.views import custom_500


@pytest.mark.django_db
def test_index_view(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.content


@pytest.mark.django_db
def test_custom_404_view(client):
    response = client.get('/page-inexistante/')
    assert response.status_code == 404
    assert b"<!DOCTYPE html>" in response.content


def test_custom_500_view():
    request = HttpRequest()
    response = custom_500(request)
    assert response.status_code == 500
    assert b"<!DOCTYPE html>" in response.content
