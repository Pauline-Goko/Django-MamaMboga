from django.shortcuts import render
from .forms import CartViewForm
from .models import Cart
from django.shortcuts import redirect


# Create your views here.

def view_cart(request):
    if request.method == 'POST':
         form = CartViewForm(request.POST, request.FILES)
         if form.is_valid():
              form.save()

    else:
         form = CartViewForm()

    return render(request, "cart/cart_upload.html", {"form": form})




def cart_list(request):
     carts = Cart.objects.all()
     return render(request, "cart/cart_list.html", {"carts": carts})


def cart_details(request, id):
     cart = Cart.objects.get(id=id)
     return render(request, "cart/cart_detail.html", {"cart": cart})



def edit_cart(request, id):
    cart = Cart.objects.get(id=id)
    if request.method == "POST":
        form = CartViewForm(request.POST, instance=cart)
        form.is_valid()
        form.save()
        return redirect("cart_list_view", id=cart)
    
    else:
        form = CartViewForm(instance=cart)

    return render(request, "cart/edit_cart.html", {"cart": cart}) 



