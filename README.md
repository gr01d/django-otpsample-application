## [django-otpsample-application](https://github.com/gr01d/django-otpsample-application)
An attempt to harden django application by using the following:
* django-otp
* django-simple-captcha
* django-admin-env-notice
* django-admin-honeypot

### Requirements:
```
Django==2.2.17
django-otp
django-simple-captcha
qrcode
django-admin-env-notice
django-admin-honeypot
```

### Commands for development (Not for Deployment)
```
$ sudo apt install python3-venv

$ python3 -m venv myvenv

$ source myvenv/bin/activate

$ python3 -m pip install -r requirements.txt

$ python3 manage.py migrate

$ python3 manage.py createsuperuser

$ python3 ./manage.py addstatictoken <username>

$ python3 manage.py runserver
```

## How

### For superuser level accounts

Note: Always login on <your-secret-admin-url> only (Line 36 mysite/urls.py)! not /login or /admin

1. After creating the super user, execute addstatictoken for the user.

2. Navigate to <your-secret-admin-url>  login with that one time use token.

3. Go to the the Admin Dashboard > Otp_Totp > TOTP devices > Add. Fields are self explanatory, generate your OTP codes using your mobile device by scanning the QR Code.

### For user level accounts (non staff/admin)

1. Login with the /login and not <your-secret-admin-url>

## TO DO

- Clean code

- Code review

- add django-user-sessions


## License

GNU AGPL v3

## Credits/References/Tutorials

[5 ways to make django admin safer](https://hackernoon.com/5-ways-to-make-django-admin-safer-eb7753698ac8)

[django-otp](https://github.com/django-otp/django-otp)

[django-simple-captcha](https://github.com/mbi/django-simple-captcha)

https://stackoverflow.com/questions/52026453/django-custom-login-form-is-valid-but-no-error/

https://www.reddit.com/r/djangolearning/comments/hmnhhz/django_2fa_otp_and_recaptcha_v3_on_the_admin/

[10-tips-making-django-admin-more-secure](https://opensource.com/article/18/1/10-tips-making-django-admin-more-secure)
