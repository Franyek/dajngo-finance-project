from django.shortcuts import render

from .models import Author


def details(request):
    all_authors = Author.objects.order_by('user_name')
    context = {
        "all_authors": all_authors
    }
    return render(request, 'about/details.html', context)
