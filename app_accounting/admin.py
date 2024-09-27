from django.contrib import admin
from .models import currency,chart_acct

class currencyAdmin(admin.ModelAdmin):
  list_display=('curr','curr_desc','date_created')
  ordering=('curr',)
  list_editable =('curr_desc',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class chrtacct_Admin(admin.ModelAdmin):
  list_display=('chrt_user','chrt_accno','chrt_desc','chrt_H_D','chrt_curr','beg_bal_formatted','beg_bal','date_created')
  
  ordering=('chrt_accno',)
  list_editable =('chrt_accno','chrt_desc','chrt_H_D','chrt_curr','beg_bal',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()  

# Register your models here.
admin.site.register(currency, currencyAdmin)
admin.site.register(chart_acct, chrtacct_Admin)