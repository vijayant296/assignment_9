from django import forms
from rest_api_app.models import Techie


class TechieForm(forms.ModelForm):
    class Meta:
        model = Techie
        fields = "__all__"

    def clean_techie_salary(self):
        inputsal = self.cleaned_data["techie_salary"]
        if inputsal < 100000:
            raise forms.ValidationError('Minimum salary should be more than 1000000')
        return inputsal

