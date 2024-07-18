from django.contrib import admin
from django.urls import include, re_path,path
from app_sample import views

app_name='app_sample'

urlpatterns = [
  path('date-sample/',views.date_sample, name='date-sample'),
 
]