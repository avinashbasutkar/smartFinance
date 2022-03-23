from curses.ascii import HT
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse
from django.template import loader

from .models import ExpenseGroup, Expense, GroupMembers
from .forms import ExpenseForm, ExpenseGroupForm, GroupCreationForm

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
        group = ExpenseGroup.objects.create(group_name = group_name, group_creation_date = timezone.now())
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
        groupMember = GroupMembers.objects.get(id=pk)
        groupMemberName = groupMember.group_member_name
    except GroupMembers.DoesNotExist:
        groupMemberName = "No Group Members Yet"
    context = {
        'ExpenseGroup': ExpenseGroup,
        'expenseGroupForm': expenseGroupForm,
        'groupName': groupName,
        # 'groupMember': groupMember,
        'groupMemberName': groupMemberName
    }
    return render(request, 'smartFinance/groupDetail.html', context)

def addExpense(request):    
    return render(request, 'smartFinance/addExpense.html')

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
  