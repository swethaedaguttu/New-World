"""
URL configuration for community_connect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# community_connect/urls.py

# community_connect/urls.py

from django.contrib import admin
from django.urls import path, include
from events import views  # Import views from the 'events' app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),  # Include the app's URL patterns at the root
    path('accounts/', include('allauth.urls')),
]







