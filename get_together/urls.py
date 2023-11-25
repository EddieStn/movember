from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_together_list, name='get_together_list'),
    path('<int:get_together_id>/', views.get_together_detail, name='get_together_detail'),
    path('create/', views.create_get_together, name='create_get_together'),
    path('edit/<int:get_together_id>/', views.edit_get_together, name='edit_get_together'),
    path('delete/<int:get_together_id>/', views.delete_get_together, name='delete_get_together'),
    path('register/<int:get_together_id>/', views.register_for_get_together, name='register_for_get_together'),
    path('withdraw/<int:get_together_id>/', views.withdraw_from_get_together, name='withdraw_from_get_together'),
]
