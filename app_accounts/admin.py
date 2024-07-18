from django.contrib import admin
from .models import UserProfile, UserAccess 

class UserProfileAdmin(admin.ModelAdmin):
  list_display=('user','avatar','cover_photo','age','location','updated','created')
  ordering=('user',)
  list_editable =('age','location',)
  filter_horizontal=()
  list_filter =()
  fieldsets=()

class UserAccessAdmin(admin.ModelAdmin):
  list_display=('user','new_user','article_create','programmer_access','article_delete')
  ordering=('user',)
  list_editable =('new_user','article_create','programmer_access', 'article_delete')
  filter_horizontal=()
  list_filter =()
  fieldsets=()  


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(UserAccess,UserAccessAdmin)
