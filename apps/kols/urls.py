from django.urls import path
from django.views.generic import TemplateView
from . import ajax_datatable_views

from apps.kols.views import KolsListView
from .ajax_datatable_views import SpecialtyAutocomplete
from .forms import SpecialtyAutoCompleteForm

app_name = 'kols'

urlpatterns = [
    path("", TemplateView.as_view(template_name='table.html'), name='table'),
    path("data/", KolsListView.as_view(), name='table_data'),
    path('ajax_datatable/',
         TemplateView.as_view(
            template_name='ajax_table.html',
            extra_context={'form_specialty': SpecialtyAutoCompleteForm()}),
            name='ajax_datatable',
     ),
    path('ajax_datatable/kols-data/',
         ajax_datatable_views.KolsAjaxDatatableView.as_view(),
         name="ajax_datatable_kols"),
    path(
        r'country-autocomplete/$',
        SpecialtyAutocomplete.as_view(),
        name='specialty-autocomplete',
    ),
]
