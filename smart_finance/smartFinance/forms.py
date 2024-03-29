from email.policy import default
from django import forms

from .models import *
from django.forms import ModelForm

class GroupCreationForm(forms.Form):
    group_name = forms.CharField(max_length=200)
    group_member_name = forms.CharField(max_length=200)

class AddExpenseForm(forms.Form):
    expense_name = forms.CharField(max_length=200)
    expense_amount = forms.IntegerField()
    

class ExpenseGroupForm(ModelForm):
    class Meta:
        model = ExpenseGroup
        fields = '__all__'

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'