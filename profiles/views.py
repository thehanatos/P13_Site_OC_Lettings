from django.shortcuts import render, get_object_or_404
from .models import Profile
import logging

"""
Views for the profiles application.

Provides views to display all profiles and individual profile details.
"""

logger = logging.getLogger(__name__)


def index(request):
    """
    Display a list of all user profiles.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered HTML page showing all profiles.
    """
    logger.info("Chargement de la page index des profils.")
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Display the details of a specific user profile.

    Args:
        request (HttpRequest): The incoming HTTP request.
        username (str): The username of the profile to display.

    Returns:
        HttpResponse: Rendered HTML page for the specific profile.
    """
    try:
        profile = get_object_or_404(Profile, user__username=username)
        logger.info(f"Affichage du profil : {profile.user.username}")
    except Exception as e:
        logger.error(f"Erreur lors de la récupération du profil {username} : {e}")
        raise
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
