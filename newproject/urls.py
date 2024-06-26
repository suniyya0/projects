from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profile.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Add other URL patterns as needed
]
