from django.urls import path
from .views import MonsterDetail, MonsterList

app_name = 'monster'

urlpatterns: list = [
    path('<str:slug>', MonsterDetail.as_view(), name="monster_detail"),
    path('all', MonsterList.as_view(), name='monster_list')
]