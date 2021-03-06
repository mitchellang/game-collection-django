"""game_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.forms import UserCreationForm


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('game_catalogue/', include('game_catalogue.urls')),
                  path('', RedirectView.as_view(url = 'game_catalogue/')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('accounts/success', views.user_signup_success, name = 'sign-up-success'),
                  path('accounts/', views.UserSignupView.as_view(), name = 'sign-up'),
              ] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)