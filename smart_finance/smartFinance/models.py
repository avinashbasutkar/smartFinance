import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class ExpenseGroup(models.Model):
    group_name = models.CharField(max_length=200)
    group_creation_date = models.DateTimeField('Group Creation Date')

    def __str__(self):
        return self.group_name

    def was_created_recently(self):
        return self.group_creation_date >= timezone.now() - datetime.timedelta(days=1)

class Expense(models.Model):
    expense = models.ForeignKey(ExpenseGroup, on_delete=models.CASCADE)
    expense_name = models.CharField(max_length=200)
    expense_date = models.DateTimeField('Expense Date')
    expense_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.expense_name

class GroupMembers(models.Model):
    group = models.ForeignKey(ExpenseGroup, on_delete=models.CASCADE)
    group_member_name = models.CharField(max_length=200)

    def __str__(self):
        return self.group_member_name