from django.contrib import admin
from django.urls import include, re_path,path
from app_notary import views

app_name='app_notary'

urlpatterns = [

    path('notary-entry/',views.notary_entry, name='notary-entry'),
    path('notary-edit/',views.notary_edit, name='notary-edit'),
    path('savenotary_input/',views.save_notary_input, name='save-notary'),

    path('save-notary-entry/',views.save_notary_entry, name='save-notary-entry'),
    
    path('notary-delete/',views.notary_delete, name='notary-delete'),


    path('notary-entry-modal/',views.notary_entry_modal, name='notary-entry-modal'),

    path('modal-notary-create/',views.modal_notary_create, name='modal-notary-create'),

    path('modal-notary-update/<int:pk>',views.modal_notary_update, name='modal-notary-update'),

    path('modal-notary-delete/<int:pk>',views.modal_notary_delete, name='modal-notary-delete'),
    path('category-entry/',views.category_entry, name='category-entry'),

]