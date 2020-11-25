"""
django-otpsample-application
Copyright (C) 2020 gr01d

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required
from user_sessions.views import SessionDeleteOtherView
urlpatterns = [
    path('', views.home, name='home'),
    path('captcha/', include('captcha.urls')),
    # User Profile
    path('profile/', views.profile, name='profile'),
    path('password/', views.change_password, name='change_password'),
    path('sessions/delete', login_required(views.CustomSessionDeleteOtherView.as_view()), name='session_delete_other',)
    ]
