from django.contrib import admin
from django.urls import include, re_path,path
from . import views

app_name='app_htmx'

urlpatterns = [
  path('app-htmx-main/',views.app_htmx_main, name='app-htmx-main'),



  path('app-htmx-test/',views.app_test, name='app-htmx-test'),  

  path('app-htmx-button1-refresh/',views.app_htmx_button1_refresh,name='app-htmx-button1-refresh'),  

  path('open-admin/',views.open_admin,name='open-admin'),  

  path('display-lorem/',views.display_lorem,name='display-lorem'),    

  path('button-4/',views.button_4,name='button-4'),

  path('success/',views.success,name='success'),     





]
