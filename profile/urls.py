from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-profile/', views.create_profile, name='create_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('view-profile/', views.view_profile, name='view_profile'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    # Add more URLs as needed



     
]
