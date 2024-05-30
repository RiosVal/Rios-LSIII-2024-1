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

def expenses(request):
    expenses = Expenses.objects.filter(user=request.user)
    return render(request, 'Expenses/expenses.html', {'expenses': expenses})

def expense_detail(request, expense_id):    #actualizar expense
    if request.method == 'GET':
        expense = get_object_or_404(Expenses, pk=expense_id, user=request.user)
        form = ExpenseForm(instance=expense)
        return render(request, 'Expenses/expense_detail.html',{
            'expense': expense,
            'form': form
        })
    else:
        try:
            expense = get_object_or_404(Expenses, pk=expense_id, user=request.user)
            form = ExpenseForm(request.POST, instance=expense)
            form.save()
            return redirect('expenses')
        except ValueError:
            return render(request, 'MonthlyIncome/income_detail.html',{
                'expense': expense,
                'form': form,
                'error': 'Error updating expense'
            })  

def create_expense(request):
    if request.method == 'GET':
        return render(request, "Expenses/create_expense.html", {
            'form': ExpenseForm
        })
    else:
        try:
            form = ExpenseForm(request.POST)
            print(form)
            new_expense = form.save(commit=False)
            new_expense.user = request.user
            new_expense.save()
            return redirect('expenses')
        except ValueError:
            return render(request, "Expenses/create_expense.html", {
                'form': ExpenseForm,
                'error': 'Please provide valid data'
            })

def delete_expense(request, expense_id):
    expense = get_object_or_404(Expenses, pk=expense_id, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('expenses')

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

