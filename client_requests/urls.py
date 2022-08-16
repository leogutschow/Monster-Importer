from django.urls import path
from .views import NewRequest

app_name = 'requests'

urlpatterns = [
    path('', NewRequest.as_view(), name='new_request')
]