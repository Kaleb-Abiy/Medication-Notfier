from django import forms
from .models import Medications


class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medications
        fields = ['med_name', 'indication', 'note', 'first_time', 'dosage']
