from django.contrib import admin
from django.urls import include, re_path,path
from app_cairo import views


app_name='app_cairo'

urlpatterns = [

    path('product_list/',views.product_list, name='product-list'),


    path('create/',views.product_create, name='product-create'),
    
    path('product_update/<int:pk>',views.product_update, name='product_update'),

    path('product_delete/<int:pk>',views.product_delete, name='product_delete'),

]