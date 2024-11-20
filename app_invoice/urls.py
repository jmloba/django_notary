from django.contrib import admin
from django.urls import include, re_path,path
from . import views

app_name='app_invoice'

urlpatterns = [
  
  path('create_invoice/',views.invoice_create , name ='invoice-create'),
  path('create-an-invoice/',views.create_an_invoice, name ='create-an-invoice'),
  path('save_invoice/',views.save_invoice , name ='save-invoice'),
  
  path('save_invoice2/',views.save_invoice2 , name ='save-invoice2'),
  path('invoice-edit/',views.invoice_edit , name ='invoice-edit'),
  path('invoice-edit2/',views.invoice_edit2 , name ='invoice-edit2'),
  path('invoice-delete/',views.invoice_delete , name ='invoice-delete'),
  path('invoice2-delete/',views.invoice2_delete , name ='invoice2-delete'),
  path('search-item/',views.search_item , name ='search-item'),  
  # category
  path('category-dashboard/',views.category_dashboard, name='category-dashboard'),  
  path('category-add/',views.category_add, name='category-add'),  

  path('category-delete/<int:pk>',views.category_delete, name='category-delete'),  
  
  path('category-update/<int:pk>',views.category_update, name='category-update'),  
  #   master
path('master-dashboard/',views.master_dashboard, name='master-dashboard'),  

path('masterfile-add/',views.masterfile_add, name='masterfile-add'),  

path('masterfile-delete/<int:pk>',views.masterfile_delete, name='masterfile-delete'),  

path('masterfile-update/<int:pk>',views.masterfile_update, name='masterfile-update'),  

  #   sales entry
path('sales-entry-dashboard/',views.sales_entry_dashboard, name='sales-entry-dashboard'),  

path('sales-entry-add/',views.sales_entry_add, name='sales-entry-add'),    
path('sales-entry-delete/<int:pk>',views.sales_entry_delete, name='sales-entry-delete'),   





 ]
