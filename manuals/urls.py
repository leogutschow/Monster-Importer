from django.urls import path
from .views import ManualDownload

app_name = 'manuals'

urlpatterns = [
    path('/download', ManualDownload.as_view(), name='manual_download')
]