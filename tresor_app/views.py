from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from .models import MonthlyIncome, Expenses
from .forms import IncomeForm, ExpenseForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'Authentication/signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('income')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': ('Username already exists')
                })
        return render(request, 'Authentication/signup.html', {
            'form': UserCreationForm,
            'error': ('Password does not match')
        })

def signin(request):

    if request.method == 'GET':
        return render(request, 'Authentication/signin.html', {
            'form': AuthenticationForm
        })
    else:

        user = authenticate(
            request,
            username=request.POST['username'], password=request.POST['password']
        )
        
        if user is None:
            return render(request, 'Authentication/signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('income')     

def signout(request):
    logout(request)
    return redirect('home')