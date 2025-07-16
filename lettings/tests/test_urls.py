from django.urls import reverse, resolve
from lettings.views import index


def test_index_url_resolves():
    path = reverse('lettings:index')
    assert resolve(path).func == index
