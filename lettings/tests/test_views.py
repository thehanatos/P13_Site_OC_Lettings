import pytest
from django.urls import reverse
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_index_view(client):
    address = Address.objects.create(
        number=10,
        street="Main St",
        city="Paris",
        state="FR",
        zip_code=75000,
        country_iso_code="FRA"
    )
    Letting.objects.create(title="Super Appartement", address=address)
    response = client.get(reverse('lettings:index'))
    assert response.status_code == 200
    assert b"Super Appartement" in response.content
