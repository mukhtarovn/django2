from django.contrib import auth
from django import forms

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ShopUserEditForm, ShopUserRegisterForm

# Create your views here.
from django.urls import reverse

from .forms import ShopUserLoginForm
from django.contrib.auth.forms import UserChangeForm

from .models import ShopUser


def login(request):
    title = 'вход'

    login_form = ShopUserLoginForm(data=request.POST or None)

    next_url = request.GET.get('next', '')
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            return HttpResponseRedirect(reverse('main'))
    content = {
        'title': title,
        'login_form': login_form,
        'next': next_url
    }
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm (request.POST, request.FILES)

        if register_form.is_valid ():
            register_form.save ()
            return HttpResponseRedirect (reverse ('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    content = {'title': title, 'register_form': register_form}

    return render (request, 'authapp/register.html', content)


def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm (request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid ():
            edit_form.save ()
            return HttpResponseRedirect (reverse ('auth:edit'))
    else:
        edit_form = ShopUserEditForm (instance=request.user)

    content = {'title': title, 'edit_form': edit_form}

    return render(request, 'authapp/edit.html', content)
