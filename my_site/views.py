from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django.contrib import messages
# from django.contrib.auth import authenticate, login

from .forms import FormLogin


def view_login(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    else:

        if request.method == 'POST':
            form = FormLogin(request.POST)

            if form.is_valid():
                # username = form.cleaned_data['username']
                # password = form.cleaned_data['password']

                return HttpResponseRedirect('/')

        else:
            form = FormLogin()

        context = {
            'form': form,
        }

        return render(request, 'my_site/login.html', context)