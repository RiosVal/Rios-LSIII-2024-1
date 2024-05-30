from django.contrib import admin
from .models import MonthlyIncome, Expenses

# Register your models here.
class MonthlyIncomeAdmin(admin.ModelAdmin):
    readonly_fields = ()

class ExpensesAdmin(admin.ModelAdmin):
    readonly_fields = ()
    

# Register your models here.
admin.site.register(MonthlyIncome, MonthlyIncomeAdmin)
admin.site.register(Expenses, ExpensesAdmin)