from django.urls import path, include
from . import views
urlpatterns = [

    path('captcha/', include('captcha.urls')),
    ]
