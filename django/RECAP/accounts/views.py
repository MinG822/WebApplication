from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from .forms import CustomUserChangeForm
from django.contrib.auth import login as auth_login
from IPython import embed
from django.contrib.auth import logout as auth_logout
from django.db import User
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.user.is_authenticated():
        return redirect('articles:index')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # embed()
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    form  = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/auth_form.html', context)

# 데코레이터는 함수안에 함수를 집어넣는 것과 같은 로직
def login(request):
    if not request.user.is_authenticated():
        return redirect('articles:index')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or 'articles:index')
    form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/auth_form.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@require_POST
def delete(request):
    request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/auth_formhtml', context)

def change_password(request):
    if request.method == "POST":
        pass