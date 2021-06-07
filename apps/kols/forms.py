from django import forms
from dal import autocomplete


class SpecialtyAutoCompleteForm(forms.Form):
    specialty = forms.ChoiceField(
        widget=autocomplete.Select2Multiple(
            url='kols:specialty-autocomplete'
        )
    )
