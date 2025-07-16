from django.db import models
from django.contrib.auth.models import User

"""
Models for the profiles application.

Defines the Profile model that extends the built-in User model with additional user-specific data.
"""


class Profile(models.Model):
    """
    Represents a user profile that extends Django's built-in User model.

    Attributes:
        user (User): One-to-one relationship with the User model.
        favorite_city (str): Optional field for the user's favorite city.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns the username of the associated user.
        """
        return self.user.username

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles_profile')
#     favorite_city = models.CharField(max_length=64, blank=True)

#     def __str__(self):
#         return self.user.username
