from django.contrib import admin
from .models import Invoice,Ref_Table,InvoiceSummary, Customer, Category_Sales, MasterFile

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
  list_display=('user','customer','invoice_no','invoice_date','itemnumber','description','quantity','price','amount')
  ordering=('-invoice_no','amount')
  list_editable =('invoice_no','invoice_date','itemnumber','description','quantity','price','amount')
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class Ref_TableAdmin(admin.ModelAdmin):
  list_display=('reference','ref_no')
  ordering=('reference',)
  list_editable =('ref_no',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class InvoiceSummaryAdmin(admin.ModelAdmin):
  list_display=('user','customer','invoice_no','invoice_date','total_quantity','total_amount','invoice_date')

  ordering=('-invoice_date','invoice_no')
  list_editable =('invoice_date','invoice_no',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class CustomerAdmin(admin.ModelAdmin):
  list_display=('user','name','phone','email','profile_pic',)

  ordering=('name','date_created')
  list_editable =('name',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class Category_SalesAdmin(admin.ModelAdmin):  
  list_display=('user','product_category','updated','created',)

  ordering=('product_category','created')
  list_editable =('product_category',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class MasterfileAdmin(admin.ModelAdmin):  
  list_display=('user','itemnumber','description','category','price', 'myimage')

  ordering=('itemnumber',)
  list_editable =('description','price')
  filter_horizontal=()
  list_filter =()
  fieldsets=()  
admin.site.register(MasterFile, MasterfileAdmin)  
admin.site.register(Category_Sales, Category_SalesAdmin)  
admin.site.register(Invoice, InvoiceAdmin)  
admin.site.register(Ref_Table, Ref_TableAdmin)  
admin.site.register(InvoiceSummary, InvoiceSummaryAdmin)  
admin.site.register(Customer, CustomerAdmin)  