## [django-otpsample-application](https://github.com/gr01d/django-otpsample-application)
An attempt to harden django application.

### Requirements:
```
Django==2.2.17
django-otp
django-simple-captcha
django-multi-captcha-admin
qrcode
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

1. After creating the super user, execute addstatictoken for the user.

2. Navigate to /admin login with that one time use token.

3. Go to the the admin dashboard > Otp_Totp > TOTP devices > Add. Fields are self explanatory, generate your OTP codes using your mobile device by scanning the QR Code.

## TO DO

- fix captcha implementation on admin or

- disable admin login

- Not logging on on some user

## Changelog

- add otp static token enabled

- enabled simple captcha admin login (overriden by OTP!)

## License

GNU AGPL v3

## Credits/References/Tutorials

[5 ways to make django admin safer](https://hackernoon.com/5-ways-to-make-django-admin-safer-eb7753698ac8)

[django-otp](https://github.com/django-otp/django-otp)

[django-simple-captcha](https://github.com/mbi/django-simple-captcha)

[django-multi-captcha-admin](https://github.com/a-roomana/django-multi-captcha-admin)
