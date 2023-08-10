from django import forms
from .models import Product


# dot to show the form is present in the form
class ProductUploadForm(forms.ModelForm):  
    class Meta:                                 #class meta within another class==tells how the main class to behave 
        model = Product
        fields = "__all__"                          # render all the fields


  
    