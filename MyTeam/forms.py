from django import forms
from .models import RezervTeamModel, RezervOstadModel


class RezervTeamForm(forms.ModelForm):
    class Meta:
        model = RezervTeamModel
        fields = ['date', 'time', 'name', 'last_name', 'phone', 'khadamat', 'id']


class RezerOstadForm(forms.ModelForm):
    class Meta:
        model = RezervOstadModel
        fields = ['date', 'time', 'name', 'last_name', 'phone', 'khadamat', 'id']
