from django import forms
from shopApp.models import Product

class ProductCreateForm(forms.ModelForm):
    #fields with validations
    class Meta:
        model=Product
        fields='__all__'
