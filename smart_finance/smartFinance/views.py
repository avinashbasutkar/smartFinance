from curses.ascii import HT
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import ExpenseGroup, Expense, GroupMembers
from .forms import AddExpenseForm, ExpenseForm, ExpenseGroupForm, GroupCreationForm

from django.contrib import messages

from django.utils import timezone

# Create your views here.

def index(request):
    group_list = ExpenseGroup.objects.order_by('group_creation_date')

    context = {
        'group_list': group_list,
    }
    return render(request, 'smartFinance/index.html', context)

def createGroup(request):
    context = {}
    context['form'] = GroupCreationForm()

    if request.method == 'POST':
        group_name = request.POST['group_name']
        group_member_name = request.POST['group_member_name']
        group = ExpenseGroup.objects.create(group_name = group_name, group_member_name = group_member_name, group_creation_date = timezone.now())
        group_member = GroupMembers.objects.create(group_member_name = group_member_name)
        messages.success(request, 'Group is created')
        return redirect('/')
    return render(request, 'smartFinance/createGroup.html', context)
   

def groupMembers(request):
    return HttpResponse("Add members to the group")

def groupDetail(request, pk):
    group = ExpenseGroup.objects.get(id=pk)
    groupName = group.group_name
    expenseGroupForm = ExpenseGroupForm(instance=group)
    try:
        # groupMember = GroupMembers.objects.get(id=pk)
        groupMemberName = group.group_member_name
    except ExpenseGroup.DoesNotExist:
        groupMemberName = "No Group Members Yet"
    context = {
        'group': group,
        'ExpenseGroup': ExpenseGroup,
        'expenseGroupForm': expenseGroupForm,
        'groupName': groupName,
        # 'groupMember': groupMember,
        'groupMemberName': groupMemberName
    }
    return render(request, 'smartFinance/groupDetail.html', context)

def groupDelete(request, pk):
    group = ExpenseGroup.objects.get(id=pk)
    groupName = group.group_name
    context = {'group': group,
    'groupName': groupName,}

    obj = get_object_or_404(ExpenseGroup, id=pk)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, 'smartFinance/groupDelete.html', context)

def addExpense(request):   
    context = {}
    context['addExpenseForm'] = AddExpenseForm()

    if request.method == 'POST':
        expense_name = request.POST['expense_name']
        expense_amount = request.POST['expense_amount']
        expense = Expense.objects.create(expense_name = expense_name, expense_amount = expense_amount, expense_date = timezone.now())
        return redirect('smartFinance/groupDetail.html')
    return render(request, 'smartFinance/addExpense.html', context)

def expenseDetail(request, pk):
    try:
        expense = Expense.objects.get(id=pk)
        expenseForm = ExpenseForm(instance=expense)
    except Expense.DoesNotExist:
        form = "This expense does not exist"

    context = {
        'Expense': Expense,
        'expenseForm': expenseForm,

    }
    return render(request, 'smartFinance/expenseDetail.html', context)

def accountDetail(request):    
    return render(request, 'smartFinance/accountDetail.html')

def login(request):    
    return render(request, 'smartFinance/login.html')
  