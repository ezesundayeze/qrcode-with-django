from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# modules for medial files
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name="home"),
    path('upload', views.upload, name='upload'),
    path('read', views.readBarcode, name='read'),

    path('api/employee', views.employeeList.as_view(), name="employee"),
    path('department/list', views.DepartmentList.as_view(), name="department"),
]
# these are the settings
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
