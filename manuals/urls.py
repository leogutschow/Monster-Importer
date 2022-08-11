from django.urls import path
from .views import ManualDownload

app_name = 'manuals'

urlpatterns = [
    path('', ManualDownload.as_view(), name='manual_download')
]