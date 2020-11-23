from django import forms
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField
from django.utils.translation import gettext_lazy as _
# Captcha #
# class LoginForm (AuthenticationForm):
#    otp_device = forms.CharField(required=False, widget=forms.Select)
#    otp_token = forms.CharField(required=False, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
#    otp_challenge = forms.CharField(required=False)
#    captcha = CaptchaField()

from django.contrib.admin.sites import AdminSite
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin.forms import AdminAuthenticationForm
from django_otp.admin import OTPAdminSite
from django_otp.forms import OTPAuthenticationFormMixin
from django.contrib import admin

# See: https://www.reddit.com/r/djangolearning/comments/hmnhhz/django_2fa_otp_and_recaptcha_v3_on_the_admin/
# https://django-otp-official.readthedocs.io/en/stable/auth.html#the-easy-way
class LoginForm(OTPAuthenticationFormMixin, AuthenticationForm):
        otp_error_messages = dict(OTPAuthenticationFormMixin.otp_error_messages,
            token_required=_('Please enter your authentication code.'),
            invalid_token=_('Incorrect authentication code. Please try again.'),
        )
        otp_device = forms.CharField(required=False, widget=forms.Select)
        otp_token = forms.CharField(required=False, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
        otp_challenge = forms.CharField(required=False)
        captcha = CaptchaField()
        def clean(self):
            self.cleaned_data = super().clean()
            self.clean_otp(self.get_user())

            return self.cleaned_data


# AdminSite.login_form = LoginForm
