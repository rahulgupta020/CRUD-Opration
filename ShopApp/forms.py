from django import forms
from .models import Productdb

class ProductForm(forms.ModelForm):
    class Meta:
        model=Productdb
        fields="__all__"