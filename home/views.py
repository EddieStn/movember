"""Home Views"""

from django.views.generic import TemplateView


class Index(TemplateView):
    """Views for the Index page"""
    template_name = 'home/index.html'
