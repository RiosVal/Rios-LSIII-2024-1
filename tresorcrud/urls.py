"""
URL configuration for tresorcrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tresor_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    #Expenses
    path('expenses/', views.expenses, name='expenses'),
    path('expenses/create/', views.create_expense, name='create_expense'),    
    path('expenses/<int:expense_id>/', views.expense_detail, name='expense_detail'),
    path('expenses/<int:expense_id>/delete', views.delete_expense, name='delete_expense'),

    #Authentication
    path('signup/', views.signup, name='signup'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin'),

    #Savings
    path('savings/', views.savings, name='savings'),

    #Income
    path('income/', views.income, name='income'),
    path('income/create/', views.create_income, name='create_income'),
    path('income/<int:income_id>/', views.income_detail, name='income_detail'),
    path('income/<int:income_id>/delete', views.delete_income, name='delete_income'),

]
