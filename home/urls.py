from django.urls import path
from .views import Index, About, Faq


urlpatterns = [
  path('', Index.as_view(), name='home'),
  path('about/', About.as_view(), name='about'),
  path('faq/', Faq.as_view(), name='faq'),
]
