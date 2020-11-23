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
from django.contrib.auth import update_session_auth_hash, authenticate, login as customlogin
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django_otp.views import LoginView

# NASTY HACK (https://stackoverflow.com/questions/52026453/django-custom-login-form-is-valid-but-no-error/)
# WIP
# See: https://www.reddit.com/r/djangolearning/comments/hmnhhz/django_2fa_otp_and_recaptcha_v3_on_the_admin/
class MyLoginView(LoginView):
    def post(self, request):
        form = LoginForm(request.user, request.POST)
        print("post")
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            human = True
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print ("USER NOT NONE")
                customlogin(request, user)
                return render(request, 'registration/login.html', {'form': form})
        else:
            print("NOT VALID")
        return render(request, 'registration/login.html', {'form': form})

        def get(self, request):
            form = LoginForm(request.user)
            print("get")
            return render(request, 'registration/login.html', {'form': LoginForm()})


@login_required(redirect_field_name='/login')
def home(request):
    return render(request, 'registration/home.html')
