from django.shortcuts import render, get_object_or_404
from .models import Letting

"""
Views for the lettings application.

Provides views to display all lettings and individual letting details.
"""


def index(request):
    """
    Display a list of all lettings.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered HTML page showing all lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Display the details of a specific letting.

    Args:
        request (HttpRequest): The incoming HTTP request.
        letting_id (int): The ID of the letting to display.

    Returns:
        HttpResponse: Rendered HTML page for the specific letting.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
