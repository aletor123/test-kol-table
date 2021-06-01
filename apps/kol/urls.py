from django.urls import path
from .views import main
app_name = 'kols'

urlpatterns = [
    path('', main, name='main')
]
