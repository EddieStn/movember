from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_profile, name='profile'),
    path('toggle-facilitator/', views.toggle_facilitator_status, name='toggle_facilitator'),
]
