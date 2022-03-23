from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('createGroup/', views.createGroup, name='createGroup'),
     path('groupMembers/', views.groupMembers, name='groupMembers'),
     path('groupDetail/<int:pk>/', views.groupDetail, name='groupDetail'),
     path('addExpense/', views.addExpense, name='addExpense'),
     path('expenseDetail/<int:pk>/', views.expenseDetail, name='expenseDetail'),
     path('accountDetail/', views.accountDetail, name='accountDetail'),
     path('login/', views.login, name='login'),
]
