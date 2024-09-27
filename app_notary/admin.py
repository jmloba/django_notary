

from django.contrib import admin
from .models import Notary_Category, Notarized_Documents, File_Serials, Notary_Posting

# Register your models here.



class notary_category_Admin(admin.ModelAdmin):
  list_display=('user','doc_category','updated','created')
  ordering=('doc_category',)
  list_editable =('doc_category',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class notarisedDocAdmin(admin.ModelAdmin):
  list_display=(
    'created','amount','is_posted',
    'firstname','lastname',
    
    'user',
    'myfile','myimage',
    'category','bookno', 'pageno', 'recordno',
    'total_tax_amount','tax_data','total_data','total_amount',
    'or_number',
    'posted_serial',
    'date_posted',
    )
  ordering=('created','user')
  list_editable =('user','firstname','lastname','is_posted','date_posted')
  filter_horizontal=()
  list_filter =()
  fieldsets=()
  

class File_Serials_Admin(admin.ModelAdmin):
  list_display=('user','serial_name','next_serial_number',)
  ordering=('serial_name',)
  list_editable =('next_serial_number',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class Notary_Posting_Admin(admin.ModelAdmin):
  list_display=('user','posted_serial','amount','tax','total_amount')
  ordering=('posted_serial',)
  list_editable =()
  filter_horizontal=()
  list_filter =()
  fieldsets=()  

admin.site.register(Notary_Posting, Notary_Posting_Admin)
admin.site.register(File_Serials, File_Serials_Admin)
admin.site.register(Notary_Category, notary_category_Admin)
admin.site.register(Notarized_Documents, notarisedDocAdmin)