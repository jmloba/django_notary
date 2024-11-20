from django.contrib import admin
from django.urls import include, re_path,path
from app_sample import views
from django.views.generic import TemplateView

from .views import chrt_List, chrtmast_Detail, chrtmast_Create, chrtmast_update,chrtmast_Delete, formview, chrtmast_templateview2, student_templateview

from .views import chrtmast_templateview, chrtmast_Create_Record,chrtmast_Update_Record, chrtmast_Delete_Record,chartmast_Details, voucherCreateView, student_DeleteRecord,studentCreateRec,studentUpdateRec


app_name='app_sample'

urlpatterns = [
  path('date-sample/',views.date_sample, name='date-sample'),
  path('appSample-Dashboard/',views.appsample_Dashboard, name='appSample-Dashboard'),
  path('create-master',views.create_master, name='create-master'),
  path('update-chrtmast/<int:pk>',views.update_chrtmast, name='update-chrtmast'),
  path('delete-record/<int:pk>',views.appsample_deleterecord, name='delete-record'),
  # listview
  path('chrt_Listview',chrt_List.as_view(), name='chrt_Listview'),
  path('chrt_detailview',chrtmast_Detail.as_view(), name='chrt_detailview'),
  path('formview',formview.as_view(), name='formview'),


# templateview sample 2
  path('chrtmast-templateview2',chrtmast_templateview2.as_view(template_name = 'app_sample/chrtmast_TemplateView2.html'),name='chrtmast-templateview2'), 


#  template view sample 
  path('template-view', chrtmast_templateview.as_view() ,name='template-view'), 

  # createview for chartmast
  path('templateview/create', chrtmast_Create_Record.as_view() ,name='chrtrec-create'), 
  path('templateview/update/<int:pk>', chrtmast_Update_Record.as_view() ,name='chrtrec-update'), 
  path('templateview/delete/<int:pk>', chrtmast_Delete_Record.as_view() ,name='chrtrec-delete'), 
  path('chrtmast-detail-<int:pk>/', chartmast_Details.as_view() ,name='chrtmast-details'), 
  # voucher create frorm
  
  path('vouchercreateview/create', voucherCreateView.as_view() ,name='voucher-create-view'), 

  #student record / sample
  path('Studentlist/', student_templateview.as_view() ,name='Studentlist-View'), 
  
  path('Studentlist/create', studentCreateRec.as_view() ,name='student-create'), 

  path('Studentlist/delete/<int:pk>', student_DeleteRecord.as_view() ,name='student-delete'), 

  path('Studentlist/update/<int:pk>', studentUpdateRec.as_view() ,name='student-update'), 


]

# https://www.youtube.com/watch?v=XGJQ4zg2RoI