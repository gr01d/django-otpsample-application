"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from app.admin import CustomOTPAdminSite
from django.contrib.auth import views as auth_views

from django_otp.forms import OTPAuthenticationForm
from app import views

from app.views import MyLoginView
from app.forms import LoginForm

admin.site.__class__ = CustomOTPAdminSite # Custom Admin with OTP and simple-captcha
admin.site.site_header = 'Dummy Administration'
admin.site.site_title = 'Dummy Administration'

urlpatterns = [
    path('', views.home, name='home'),

    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),

    path('login/', MyLoginView.as_view(authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
