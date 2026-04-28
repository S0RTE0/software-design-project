from django import forms
from .models import Cinema

class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ['name', 'description']
