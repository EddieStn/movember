"""Home, About Us and FAQs Views"""

from django.views.generic import TemplateView
from blog.models import Blog
from get_together.models import GetTogether


class Index(TemplateView):
    """Views for the Index page"""
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_event'] = GetTogether.objects.order_by('-date').first()
        context['latest_blog'] = Blog.objects.order_by('-created_at').first()

        return context

class About(TemplateView):
    """Views for the Index page"""
    template_name = 'home/about.html'

class Faq(TemplateView):
    """Views for the Index page"""
    template_name = 'home/faq.html'
