# Create your views here.

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import Element_Analytics.settings as settings
from Element_Analytics.settings import DOCUMENT_ROOT
from apps.signup.forms import UserCreateForm

import os


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user_dir = os.path.join(DOCUMENT_ROOT, user.username)
            if not os.path.exists(user_dir):
                os.mkdir(user_dir)
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = UserCreateForm()
    return render(request, 'signup/signup.djt', {'form': form})

