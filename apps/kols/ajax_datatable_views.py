from ajax_datatable.views import AjaxDatatableView
from dal.views import BaseQuerySetView
from dal_select2.views import Select2QuerySetView

from .models import Kol


class KolsAjaxDatatableView(AjaxDatatableView):
    model = Kol
    title = 'Kol'
    initial_order = [["first_name", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'
    show_column_filters = True

    column_defs = [
        {'name': 'id', 'visible': False, },
        {'name': 'first_name', 'visible': True, },
        {'name': 'last_name', 'visible': True, },
        {'name': 'middle_name', 'visible': True, },
        {'name': 'credential', 'visible': True, },
        {'name': 'specialty', 'visible': True, 'choices': True,
         'autofilter': True},
    ]


from dal import autocomplete

from .models import Kol


class SpecialtyAutocomplete(Select2QuerySetView):
    model = Kol
    search_fields = ['specialty']

    def get_result_label(self, result):
        return result.specialty

    def get_selected_result_label(self, result):
        return result.specialty