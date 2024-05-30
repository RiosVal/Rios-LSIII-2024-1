from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MonthlyIncome(models.Model):
    income_origin = models.CharField(max_length=100, blank=True, null=True)  # Nuevo
    currency = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'By ' + self.user.username

class Expenses(models.Model):
    expense_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'By ' + self.user.username

class ProjectedSavings(models.Model):
    monthly_savings_amount = models.DecimalField(max_digits=10, decimal_places=2)
    saving_time_months = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'By ' + self.user.username
