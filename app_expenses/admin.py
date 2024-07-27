from django.contrib import admin
from .models import Expense, Category
# Register your models here.



class ExpenseAdmin(admin.ModelAdmin):
  list_display=('date','amount','owner','posted','posted_by','posted_date')

  ordering=('date','amount')
  list_editable =('amount',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()




class Category_ExpenseAdmin(admin.ModelAdmin):
  list_display=('name',)

  ordering=('name',)
  list_editable =()
  filter_horizontal=()
  list_filter =()
  fieldsets=()

admin.site.register(Expense, ExpenseAdmin)  
admin.site.register(Category, Category_ExpenseAdmin)  
