from django.shortcuts import render
from .forms import OrderViewForm
from .models import Order
from django.shortcuts import redirect

# Create your views here.



def add_order(request):
    if request.method == "POST":
        form = OrderViewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = OrderViewForm()

    return render(request, "order/order_add.html", {"form": form})


def order_list(request):
    orders = Order.objects.all()
    return render(request, "order/order_list.html", {"orders": orders})


def order_details(request, id):
    order = Order.objects.get(id=id)
    return render(request, "order/order_details.html", {"order": order})


def edit_order(request, id):
    order = Order.objects.get(id=id)
    if request.method == "POST":
        form = OrderViewForm(request.POST, request.FILES)
        form.is_valid()
        form.save()
        return redirect("order")
    
    else:
        form = OrderViewForm(instance=order)
        return render(request, "order/order_edit.html", {"form": form})
