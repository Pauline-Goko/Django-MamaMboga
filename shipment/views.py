from django.shortcuts import render
from .forms import ShipmentViewForm
from .models import Shipment
from django.shortcuts import redirect

# Create your views here.


def add_shipment(request):
    if request.method == "POST":
        form = ShipmentViewForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()

    else:
        form = ShipmentViewForm()

    return render(request, "shipment/shipment_add.html", {"form": form})


def shipment_list(request):
    shipments = Shipment.objects.all()
    return render(request, "shipment/shipment_list.html", {"shipments": shipments})


def shipment_details(request, id):
    shipment = Shipment.objects.get(id=id)
    return render(request, "shipment/shipment_details.html", {"shipment": shipment})



def edit_shipment(request, id):
    shipment = Shipment.objects.get(id=id)
    if request.method == "POST":
        form = ShipmentViewForm(request.POST, request.FILES)
        form.is_valid()
        form.save()
        return redirect("shipment")
    
    else:
        form = ShipmentViewForm(instance=shipment)
        return render(request, "shipment/shipment_edit.html", {"form": form})