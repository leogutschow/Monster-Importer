from django.urls import path
from .views import DevLog

app_name = 'devlogs'

urlpatterns = [
    path('<str:slug>', DevLog.as_view(), name='update_devlog'),
]