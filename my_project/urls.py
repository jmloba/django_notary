from . import views
from django.contrib import admin

from django.urls import include,  path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home , name ='home' ),     

    
    path('app_notary/', include('app_notary.urls')),
    path('app_notary_ver2/', include('app_notary_ver2.urls')),

    
    path('app_import/', include('app_import.urls')),
    path('app_htmx/', include('app_htmx.urls')),
    path('app_accounts/', include('app_accounts.urls')),
    path('app_cairo/', include('app_cairo.urls')),
    path('app_forms/', include('app_forms.urls')),
]
if settings.DEBUG:
    urlpatterns+= staticfiles_urlpatterns()
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
