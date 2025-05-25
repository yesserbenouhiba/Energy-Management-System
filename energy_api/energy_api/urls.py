"""
URL configuration for energy_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Django admin interface (default path to manage models, users, etc.)
    path('admin/', admin.site.urls),

    # Include all API endpoints defined in the 'core' app under the '/api/' path
    path('api/', include('core.urls')),

    # Endpoint to obtain an authentication token using Django REST framework's token authentication
    path('api-token-auth/', obtain_auth_token),
]

