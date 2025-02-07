from django.shortcuts import render
from .models import About

# Create your views here.
def about_detail(request):
    """
    Renders the about page
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about_detail.html",
        {"about": about},
    )
