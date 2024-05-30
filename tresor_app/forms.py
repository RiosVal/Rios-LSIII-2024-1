from django.forms import ModelForm
from .models import MonthlyIncome, Expenses

class IncomeForm(ModelForm):
    class Meta:
        model = MonthlyIncome
        fields = [
            'income_origin',
            'currency',
            'amount'
        ]


class ExpenseForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['expense_name','amount']