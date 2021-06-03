from django.urls import path
from django.views.generic import TemplateView

from apps.kols.views import KolsListView

app_name = 'kols'

urlpatterns = [
    path("", TemplateView.as_view(template_name='table.html'), name='table'),
    path("data/", KolsListView.as_view(), name='table_data')
]