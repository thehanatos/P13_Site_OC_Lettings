from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator

"""
Models for the lettings application.

Defines the Address and Letting models used to store rental property data.
"""


class Address(models.Model):
    """
    Represents a physical address for a letting.

    Attributes:
        number (int): Street number.
        street (str): Street name.
        city (str): City name.
        state (str): 2-letter state code.
        zip_code (int): 5-digit ZIP code.
        country_iso_code (str): 3-letter ISO country code.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Returns a readable string representation of the address.
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Represents a letting (rental property) entry.

    Attributes:
        title (str): Title of the letting.
        address (Address): One-to-one relationship to an Address.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns the title of the letting.
        """
        return self.title
