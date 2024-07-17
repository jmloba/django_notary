

from django.contrib import admin
from .models import Notary_Category, Notarized_Documents

# Register your models here.



class notary_category_Admin(admin.ModelAdmin):
  list_display=('user','doc_category','updated','created')
  ordering=('doc_category',)
  list_editable =('doc_category',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class notarisedDocAdmin(admin.ModelAdmin):
  list_display=('user','amount_paid','myfile','myimage','category','firstname','lastname','created','bookno', 'pageno', 'recordno')
  ordering=('created',)
  list_editable =('firstname','lastname')
  filter_horizontal=()
  list_filter =()
  fieldsets=()
  

admin.site.register(Notary_Category, notary_category_Admin)
admin.site.register(Notarized_Documents, notarisedDocAdmin)