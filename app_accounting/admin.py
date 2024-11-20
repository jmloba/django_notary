from django.contrib import admin
from .models import currency,chart_acct,ytdfd,voucher_creation,myvalidator,CreateVoucherGroup

class currencyAdmin(admin.ModelAdmin):
  list_display=('curr','curr_desc','date_created')
  ordering=('curr',)
  list_editable =('curr_desc',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class chrtacct_Admin(admin.ModelAdmin):
  list_display=('chrt_user','chrt_accno','chrt_desc','chrt_H_D','chrt_curr','beg_bal_formatted','beg_bal','date_created',)
  
  ordering=('chrt_accno',)
  list_editable =('chrt_desc','chrt_H_D','chrt_curr','beg_bal',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()  

class ytdfd_Admin(admin.ModelAdmin):
  list_display=('user','voucherno','voucher_date','accno','dr','amount','project','date_created')
  ordering=('date_created',)

  list_editable =('voucherno','accno','amount',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()  


class voucher_creation_Admin(admin.ModelAdmin):
  list_display=('voucher_group','accno','dc','author')
  ordering=('voucher_group','accno')

  list_editable =()
  filter_horizontal=()
  list_filter =()
  fieldsets=()    

class myValidator_Admin(admin.ModelAdmin):
  list_display=('val_user','mobile_no','name','birth_date')
  ordering=('mobile_no',)

  list_editable =('mobile_no',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()    

class createvoucher_Admin(admin.ModelAdmin):
  list_display=('accno','desc','updated','created')
  ordering=('desc',)
  list_editable =('desc',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()    
# Register your models here.

admin.site.register(currency, currencyAdmin)
admin.site.register(chart_acct, chrtacct_Admin)
admin.site.register(ytdfd, ytdfd_Admin)

admin.site.register(voucher_creation, voucher_creation_Admin)
admin.site.register(myvalidator, myValidator_Admin)
admin.site.register(CreateVoucherGroup, createvoucher_Admin)


