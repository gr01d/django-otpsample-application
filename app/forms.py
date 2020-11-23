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
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField
from django.utils.translation import gettext_lazy as _

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


AdminSite.login_form = LoginForm
