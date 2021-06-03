from .models import Kol
from django_datatables_view.base_datatable_view import BaseDatatableView


class KolsListView(BaseDatatableView):
    # The model we're going to show
    model = Kol

    # define the columns that will be returned
    columns = ['first_name', 'middle_name', 'last_name', 'credential',
               'specialty']
