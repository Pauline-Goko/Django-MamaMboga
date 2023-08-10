from django.shortcuts import render
from .forms import PaymentViewForm
from .models import Payment
from django.shortcuts import redirect


# Create your views here.

def add_payment(request):
    if request.method == "POST":
        form = PaymentViewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PaymentViewForm()

    return render(request, "payment/payment_add.html", {"form": form})


def payment_list(request):
    payments = Payment.objects.all()
    return render(request, "payment/payment_list.html", {"payments": payments})


def payment_details(request, id):
    payment = Payment.objects.get(id=id)
    return render(request, "payment/payment_details.html", {"payment": payment})



def edit_payment(request, id):
    payment = Payment.objects.get(id=id)
    if request.method == "POST":
        form = PaymentViewForm(request.POST, request.FILES)
        form.is_valid()
        form.save()
        return redirect("payment")
    
    else:
        form = PaymentViewForm(instance=payment)
        return render(request, "payment/payment_edit.html", {"form": form})