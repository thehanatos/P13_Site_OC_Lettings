import pytest
from django.urls import reverse
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_letting_page_displays_full_data(client):
    address = Address.objects.create(
        number=10,
        street="Rue du Test",
        city="Lyon",
        state="FR",
        zip_code=69000,
        country_iso_code="FRA"
    )
    letting = Letting.objects.create(title="Grand Appartement", address=address)

    url = reverse("lettings:index")
    response = client.get(url)

    assert response.status_code == 200
    assert letting.title.encode() in response.content
    assert letting.address.street.encode() in response.content
