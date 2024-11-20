


from django.contrib import admin
from django.urls import include, re_path,path
from app_accounting import views
from .views import voucherCreation_ListView,voucherCreation_DeleteView,voucherCreation_Create,voucherCreation_UpdateView


app_name='app_accounting'

urlpatterns = [
# chart of accounts
    path('acct-dashboard/',views.acct_dashboard, name='acct-dashboard'),

    path('create-master/',views.create_master, name='create-master'),    
    
    path('create-master-modal/',views.create_master_modal, name='create-master-modal'),   

    path('create-master-ajax/',views.create_master_ajax, name='create-master-ajax'),      

    path('submitCreateNewRecord/',views.submitCreateNewRecord, name='submitCreateNewRecord'),       

    path('delete-record/<int:pk>',views.delete_record, name='delete-record'),    

    path('update-record/<int:pk>',views.update_record, name='update-record'),    

# vouchercreation
    path('acct-dashboard-voucher-creation/',views.acct_dashboard_voucher_creation, name='acct-dashboard-voucher-creation'),


    path('delete-vouchergroup-record/<int:pk>',views.delete_vouchergroup_record, name='delete-vouchergroup-record'),   

    path('create-voucher-group/',views.create_voucher_group, name='create-voucher-group'),    

    path('update-vouchergroup-record/<int:pk>',views.update_vouchergroup_record, name='update-vouchergroup-record'),  
# vouchercreation class based 
    path('vouchergroup/',voucherCreation_ListView.as_view(), name='voucher-creation-listview'),
    
    path('vouchergroup/delete/<int:pk>',voucherCreation_DeleteView.as_view(), name='vouchercreation-deleteview'),

    path('vouchergroup/create',voucherCreation_Create.as_view(), name='vouchercreation-createview'),
    
    path('vouchergroup/update/<int:pk>',voucherCreation_UpdateView.as_view(), name='vouchercreations-updateview'),
    
# validator
    path('acct-dashboard-myvalidator/',views.acct_dashboard_myvalidator, name='acct-dashboard-myvalidator'),    

    path('myvalidator-create-record/',views.myvalidator_create_record, name='myvalidator-create-record'),        

    path('myvalidator-delete-record/<int:pk>',views.myvalidator_delete_record, name='myvalidator-delete-record'),    

    path('myvalidator-update-record/<int:pk>',views.myvalidator_update_record, name='myvalidator-update-record'),    

#orm queries    (table : CreateVoucherGroup)
    path('orm-dashboard/',views.orm_dashboard, name='orm-dashboard'), 

    path('vouchergroup-test-createrecord',views.vouchergroup_test_createrecord, name='vouchergroup-test-createrecord'), 

    path('vouchergroup-test-deleterecord/<int:pk>',views.vouchergroup_test_deleterecord, name='vouchergroup-test-deleterecord'), 
# orm querysets
    path('update-queryset',views.update_queryset, name='update-queryset'), 

    path('queryset-filter-startwith',views.queryset_filter_startwith, name='queryset-filter-startwith'), 

    path('queryset-usingQ',views.queryset_usingQ, name='queryset-usingQ'), 
 

    path('get-accname',views.get_accname, name='get-accname'), 
# popup  returns value  
    path('sample-popup-return-value',views.sample_popup_return_value, name='sample-popup-return-value'),

    
]