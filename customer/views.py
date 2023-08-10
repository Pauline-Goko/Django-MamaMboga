from django.shortcuts import render
from .forms import CustomerViewForm
from .models import Customer
from django.shortcuts import redirect

# Create your views here.


def add_customer(request):
    if request.method == "POST":
        form =  CustomerViewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = CustomerViewForm()

    return render(request, "customer/customer_add.html", {"form": form})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "customer/customer_list.html", {"customers": customers})



def customer_details(request, id):
     customer = Customer.objects.get(id=id)
     return render(request, "customer/customer_details.html", {"customer": customer})

    
def edit_customer(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == "POST":
        form = CustomerViewForm(request.POST, instance=customer)
        form.is_valid()
        form.save()
        return redirect("customer")
        
    
    else:
        form = CustomerViewForm(instance=customer)
        return render(request, "customer/customer_edit.html", {"form": form})