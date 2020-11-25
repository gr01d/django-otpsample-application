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

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

from django.views.generic import DeleteView, ListView, View
from django.views.generic.edit import DeletionMixin
from user_sessions.views import LoginRequiredMixin, SessionMixin
from django.urls import reverse_lazy


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

# Fake page
@login_required(redirect_field_name='/login')
def blank(request):
    return render(request, 'registration/404.html')

# https://simpleisbetterthancomplex.com/tips/2016/08/04/django-tip-9-password-change-form.html
@login_required(redirect_field_name='/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'app/change_password.html', {
        'form': form
    })

# User Profile View
@login_required(redirect_field_name='/login')
def profile(request):
    usermodel = User.objects.get( username=request.user)
    # Get All Current User Sessions
    object_list = request.user.session_set.all()
    return render(request, 'app/profile.html', {'usermodel': usermodel, 'object_list': object_list})

# django-user-sessions views.py
class CustomSessionDeleteOtherView(LoginRequiredMixin, SessionMixin, DeletionMixin, View):
    """
    View for deleting all user's sessions but the current.

    This view allows a user to delete all other active session. For example
    log out all sessions from a computer at the local library or a friend's
    place.
    """
    def get_object(self):
        return super(CustomSessionDeleteOtherView, self).get_queryset().\
            exclude(session_key=self.request.session.session_key)

    def get_success_url(self):
        return str(reverse_lazy('profile'))
