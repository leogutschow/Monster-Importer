from django.urls import path
from .views import DevLogDetail, DevLogList

app_name = 'devlogs'

urlpatterns = [
    path('all', DevLogList.as_view(), name='devlog_list'),
    path('<str:slug>', DevLogDetail.as_view(), name='update_devlog'),
]
