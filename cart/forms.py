from django import forms
from .models import Cart


class CartViewForm(forms.ModelForm):  
    class Meta:                                 #class meta within another class==tells how the main class to behave 
        model = Cart
        fields = "__all__"    