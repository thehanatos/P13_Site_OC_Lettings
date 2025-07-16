from django.shortcuts import render
import logging


logger = logging.getLogger(__name__)


def index(request):
    """
    Home page view for the site.
    """
    return render(request, 'index.html')


def custom_404(request, exception):
    """
    Custom view for handling 404 errors.
    """
    return render(request, '404.html', status=404)


def custom_500(request):
    """
    Custom view for handling 500 errors.
    """
    logger.critical("Erreur serveur interne (500)")
    return render(request, '500.html', status=500)
