


from django.contrib import admin
from django.urls import include, re_path,path
from app_accounting import views

app_name='app_accounting'

urlpatterns = [
# notary documents
    path('acct-dashboard/',views.acct_dashboard, name='acct-dashboard'),

 
    path('create-master/',views.create_master, name='create-master'),    

    path('delete-record/<int:pk>',views.delete_record, name='delete-record'),    
    path('update-record/<int:pk>',views.update_record, name='update-record'),    


]