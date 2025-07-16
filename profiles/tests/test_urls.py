from django.urls import reverse, resolve
from profiles.views import index


def test_index_url_resolves():
    path = reverse('profiles:index')
    assert resolve(path).func == index
