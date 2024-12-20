
from django.contrib import admin
from django.urls import include, re_path,path
from app_forms import views
from .views import notary_create_record,NotaryDashboardListview,NotaryCreateView,NotaryDeleteView, NotaryUpdateView

app_name='app_forms'

urlpatterns = [
# notary documents
    path('dashboard/',views.dashboard, name='dashboard'),
    path('create-record/',views.create_record, name='create-record'),    
    path('create-record-modal/',views.create_record_modal, name='create-record-modal'),    
    path('update-record/<int:pk>',views.update_record, name='update-record'),    
    path('delete-record/<int:pk>',views.delete_record, name='delete-record'),    

# templateview
#     
    path('notary/create-record',notary_create_record.as_view(), name='notary-create-record'),    
# Category

    path('category-dashboard/',views.category_dashboard, name='category-dashboard'),
    path('create-record-category/',views.create_record_category, name='create-record-category'),    
    path('update-category-record/<int:pk>',views.update_category_record, name='update-category-record'),  
    path('delete-category-record/<int:pk>',views.delete_category_record, name='delete-category-record'),  
    
#  Propvince / Towns
    path('provtown-dashboard/',views.provtown_dashboard, name='provtown-dashboard'),
# 
    path('post-entries/',views.post_entries, name='post-entries'),
    
#  sales report   
    path('sales-report-posted/',views.sales_report_posted, name='sales-report-posted'),

    path('print-posted-filter/',views.print_posted_filter, name='print-posted-filter'),


#  listview
    path('notarysales-dashboard/',NotaryDashboardListview.as_view(), name='notarysales-dashboard'),
#   createview    
    path('notarysales-createview/',NotaryCreateView.as_view(), name='notarysales-createview'),


    path('notarysales/<int:pk>/delete/',NotaryDeleteView.as_view(), name='notarysales-deleteview'),

    path('notarysales/<int:pk>/update/',NotaryUpdateView.as_view(), name='notarysales-updateview'),

]
    
