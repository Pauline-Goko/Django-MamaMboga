from django import forms
from .models import Shipment


class ShipmentViewForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = "__all__"