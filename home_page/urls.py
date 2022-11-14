from django.urls import path
from .views import Index, About, TermsOfUse

app_name = 'home'

urlpatterns = [
    path('', Index.as_view(), name='home_page'),
    path('about', About.as_view(), name='about'),
    path('terms', TermsOfUse.as_view(), name='terms')
]