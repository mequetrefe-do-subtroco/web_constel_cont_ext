from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib import messages
import requests

CONSTEL_WEB_LOGIN_URL = 'constel.herokuapp.com/almoxarifado/cont/api/login/'


class AuthenticationBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        if username is None:
            username = kwargs.get(User().USERNAME_FIELD)

        if username is None or password is None:

            return

        payload = {
            'username': username,
            'password': password,
        }

        response = requests.post(CONSTEL_WEB_LOGIN_URL, json=payload)

        if response.status_code == 200:
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)

            else:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                )
                user.save()

            return user

        elif response.status_code == 400:
            messages.error(request, 'Usuário e/ou senha incorretos')

            return None

        else:
            messages.error(request, 'Falha na conexão com o sistema Constel.tk')

            return None
