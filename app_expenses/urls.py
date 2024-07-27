
from django.contrib import admin
from django.urls import include, re_path,path
from app_expenses import views


app_name='app_expenses'

urlpatterns = [
    path('expense-dashboard/',views.expense_dashboard, name='expense-dashboard'),  
    
    path('create-expense-rec/',views.create_expense_rec, name='create-expense-rec'),  
    
    path('expenses-add/',views.expenses_add, name='expenses-add'),  

    path('expenses-delete/<int:pk>',views.expenses_delete, name='expenses-delete'),  
    path('expenses-update/<int:pk>',views.expenses_update, name='expenses-update'),  
]