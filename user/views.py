from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.models import User
from .models import * 
from django.contrib import messages
from datetime import datetime
from django.utils import timezone


def UserRegister(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.created_date = timezone.now()
            user.save()
            login(request, user)
            
            messages.success(request,
                             'Təbriklər,uğurla qeydiyyatdan keçdiniz!Xahiş edirik mailinizə gələn mesajı təsdiq edəsiniz!')
            return HttpResponseRedirect('/')


    else:
        form = RegisterForm()
        
    context['form'] = form
    return render(request, 'register.html', context)



def login_view(request):
    context = {}
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect('blog:index')
    context['form'] = form
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('blog:index')


def Contact_view(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            teklif = form.save(commit=False)
            teklif.user = request.user
            teklif.created_date = timezone.now()
            teklif.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
        
    context['form'] = form
    return render(request, 'contact.html', context)
