import pytest
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_str():
    address = Address.objects.create(
        number=12,
        street="Main Street",
        city="Paris",
        state="FR",
        zip_code=75001,
        country_iso_code="FRA"
    )
    assert str(address) == "12 Main Street"


@pytest.mark.django_db
def test_letting_str():
    address = Address.objects.create(
        number=45,
        street="Broadway",
        city="NYC",
        state="NY",
        zip_code=10001,
        country_iso_code="USA"
    )
    letting = Letting.objects.create(title="Nice Flat", address=address)
    assert str(letting) == "Nice Flat"
