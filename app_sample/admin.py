from django.contrib import admin


from .models import StudentRec
class StudentRecAdmin(admin.ModelAdmin):
  list_display=('studno','firstname','lastname','birthdate','mobile','notes')
  ordering=('studno',)
  list_editable =('firstname','lastname','notes','mobile')
  filter_horizontal=()
  list_filter =()
  fieldsets=()

admin.site.register(StudentRec, StudentRecAdmin)
# Register your models here.
