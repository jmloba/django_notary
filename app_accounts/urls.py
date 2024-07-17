
from django.urls import path, re_path
from django.contrib import admin

from . import views

app_name='app_accounts'

urlpatterns = [
  path('login/',views.login_view, name='login-view'),
  path('register/',views.register_view, name='register-view'), 

  path('forgot_password/',views.forgot_password, name='forgot-password'),  
  path('logout/',views.logout_view, name='logout-view'),  
  
  path('reset_Password_validate/<uidb64>/<token>/', views.reset_Password_validate, name ='reset_Password_validate'),       
  
  path('reset_password/',views.reset_Password, name='reset_Password'),  

  
]
