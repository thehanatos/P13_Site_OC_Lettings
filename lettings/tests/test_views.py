import pytest
from django.urls import reverse
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_letting_detail_view(client):
    address = Address.objects.create(
        number=42,
        street="Rue de Test",
        city="Bordeaux",
        state="FR",
        zip_code=33000,
        country_iso_code="FRA"
    )
    letting = Letting.objects.create(title="Appartement Bordeaux", address=address)

    url = reverse('lettings:letting', kwargs={'letting_id': letting.id})
    response = client.get(url)

    assert response.status_code == 200
    assert letting.title.encode() in response.content
    assert letting.address.street.encode() in response.content
