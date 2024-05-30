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
