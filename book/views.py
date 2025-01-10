from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

# Create your views here.
class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'book/index.html'


