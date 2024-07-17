from django.contrib import admin
from django.urls import include, re_path,path
from app_notary_ver2 import views

app_name='app_notary_ver2'

urlpatterns = [
    path('notaryv2-entry-modal/',views.notaryv2_entry_modal, name='notaryv2-entry-modal'),

    path('modal-v2-notary-create/',views.modal_v2_notary_create, name='modal-v2-notary-create'),  

    path('modal-v2-notary-update/<int:pk>',views.modal_v2_notary_update, name='modal-v2-notary-update'),

    path('modal-v2-notary-delete/<int:pk>',views.modal_v2_notary_delete, name='modal-v2-notary-delete'),

]
