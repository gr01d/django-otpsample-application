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
from django.contrib import admin
# Register your models here.
from django import forms
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.admin.sites import AdminSite

from .forms import OTPAuthenticationFormMixin
from captcha.fields import CaptchaField

def _admin_template_for_django_version():
    """
    Returns the most appropriate Django login template available.

    In the past, we've had more version-specific templates. Perhaps this will
    be true again in the future. For now, the Django 1.11 version is suitable
    even with the most recent Django version.
    """
    return 'registration/login.html'


class CustomOTPAdminAuthenticationForm(AdminAuthenticationForm, OTPAuthenticationFormMixin):
    """
    An :class:`~django.contrib.admin.forms.AdminAuthenticationForm` subclass
    that solicits an OTP token. This has the same behavior as
    :class:`~django_otp.forms.OTPAuthenticationForm`.
    """
    otp_device = forms.CharField(required=False, widget=forms.Select)
    otp_token = forms.CharField(required=False)

    # This is a placeholder field that allows us to detect when the user clicks
    # the otp_challenge submit button.
    otp_challenge = forms.CharField(required=False)
    captcha = CaptchaField()

    def clean(self):
        self.cleaned_data = super().clean()
        self.clean_otp(self.get_user())

        return self.cleaned_data


class CustomOTPAdminSite(AdminSite):
    """
    This is an :class:`~django.contrib.admin.AdminSite` subclass that requires
    two-factor authentication. Only users that can be verified by a registered
    OTP device will be authorized for this admin site. Unverified users will be
    treated as if :attr:`~django.contrib.auth.models.User.is_staff` is
    ``False``.
    """
    #: The default instance name of this admin site. You should instantiate
    #: this class as ``OTPAdminSite(OTPAdminSite.name)`` to make sure the admin
    #: templates render the correct URLs.
    name = 'otpadmin'

    login_form = CustomOTPAdminAuthenticationForm

    #: We automatically select a modified login template based on your Django
    #: version. If it doesn't look right, your version may not be supported, in
    #: which case feel free to replace it.
    login_template = _admin_template_for_django_version()

    def __init__(self, name='otpadmin'):
        super().__init__(name)

    def has_permission(self, request):
        """
        In addition to the default requirements, this only allows access to
        users who have been verified by a registered OTP device.
        """
        return super().has_permission(request) and request.user.is_verified()
