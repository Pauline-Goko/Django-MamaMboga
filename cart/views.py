from django.shortcuts import render
from .forms import CartViewForm
from .models import Cart
from django.shortcuts import redirect
from .models import Product



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








def remove_product_from_cart(request, cart_id, product_id):
    cart = Cart.objects.get(id=cart_id)
    product = Product.objects.get(id=product_id)
    
    try:
        cart_item = Cart.objects.get(cart=cart, product=product)
        cart_item.delete()
    except Cart.DoesNotExist:
        pass
    
    # Redirect back to the cart or wherever you want
    return redirect('cart/cart_detail.html')  # Replace 'cart_view' with the appropriate URL name

