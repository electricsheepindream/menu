from django import forms
from .models import Restaurants


class ResForm(forms.ModelForm):
    class Meta:
        model = Restaurants
        fields = ['name',
                  'location',
                  'manager',
                  'type',
                  ]