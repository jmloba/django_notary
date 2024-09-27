from django.contrib import admin
from .models import Invoice,Ref_Table,InvoiceSummary,Category_Sales, Customer, Master, Tax

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

class CategorySales_Admin(admin.ModelAdmin):
  list_display=('category',)

  ordering=('category',)
  list_editable =()
  filter_horizontal=()
  list_filter =()
  fieldsets=()
 

class Master_Admin(admin.ModelAdmin):
  list_display=('user','itemnumber','description','myimage')

  ordering=('itemnumber',)
  list_editable =()
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class Tax_Admin(admin.ModelAdmin):
  list_display=('tax_type','tax_percentage','is_active')

  ordering=('tax_type',)
  list_editable =()
  filter_horizontal=()
  list_filter =()
  fieldsets=() 
admin.site.register(Tax,Tax_Admin)  

admin.site.register(Master,Master_Admin )  
admin.site.register(Category_Sales,CategorySales_Admin )  

admin.site.register(Customer, CustomerAdmin)  

admin.site.register(InvoiceSummary,  InvoiceSummaryAdmin)  

admin.site.register(Invoice, InvoiceAdmin)  
admin.site.register(Ref_Table, Ref_TableAdmin) 
