
from django.contrib import admin
from django.urls import include, re_path,path
from app_forms import views

app_name='app_forms'

urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),

    path('create-record/',views.create_record, name='create-record'),    

    path('update-record/<int:pk>',views.update_record, name='update-record'),    
    path('delete-record/<int:pk>',views.delete_record, name='delete-record'),    

]
    
