from django.contrib import admin
from django.urls import include, re_path,path
from . import views

app_name='app_import'

urlpatterns = [
  path('import-excel-city/',views.import_excel_city, name='import-excel-city'),

  path('import-city/',views.import_city_now, name='import-city'),

  path('city-delete/',views.city_delete, name='city-delete'),
  

  path('import-province-town/',views.import_province_town, name='import-province-town'),  
  path('province-town-delete/',views.province_town_delete, name='province-town-delete'),  


]
