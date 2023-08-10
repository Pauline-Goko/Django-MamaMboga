from django.shortcuts import render
from .forms import VendorViewForm
from .models import Vendor
from django.shortcuts import redirect

# Create your views here.


def add_vendor(request):
    if request.method == "POST":
        form = VendorViewForm(request.POST, request.FILES)
        form.is_valid()
        form.save()

    else:
        form = VendorViewForm()

    return render(request, "vendor/vendor_add.html", {"form": form})


def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, "vendor/vendor_list.html", {"vendors": vendors})



def vendor_details(request, id):
    vendor = Vendor.objects.get(id=id)
    return render(request, "vendor/vendor_details.html", {"vendor": vendor})


def edit_vendor(request, id):
    vendor = Vendor.objects.get(id=id)
    if request.method == "POST":
        form = VendorViewForm(request.POST, request.FILES)
        form.is_valid()
        form.save()
        return redirect("vendor")
    
    else:
        form = VendorViewForm(instance=vendor)
        return render(request, "vendor/vendor_edit.html", {"form": form})
    