

from django.contrib import admin
from .models import Phil_City ,Phil_Province_Towns
from import_export.admin import ImportExportModelAdmin

# Register your models here.



class PhilCityAdmin(ImportExportModelAdmin):
  list_display=('country','province','city','is_active','created_at')
  ordering=('province','city')
  list_editable =('city',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class PhilTownsAdmin(ImportExportModelAdmin):
  list_display=('country','province','towns','is_active','created_at')
  ordering=('province','towns')
  list_editable =('towns',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()
    

admin.site.register(Phil_City, PhilCityAdmin)

admin.site.register(Phil_Province_Towns, PhilTownsAdmin)
