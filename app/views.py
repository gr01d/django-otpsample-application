from django.contrib.auth import update_session_auth_hash, authenticate, login as customlogin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django_otp.forms import OTPTokenForm
from django_otp.views import LoginView
from django_otp import match_token


from functools import partial

from django.contrib.auth import BACKEND_SESSION_KEY
from django.contrib.auth import views as auth_views
from django.utils.functional import cached_property

from django_otp.forms import OTPAuthenticationForm, OTPTokenForm

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
