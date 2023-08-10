from django.shortcuts import render 
from .forms import ProductUploadForm
from .models import Product
from django.shortcuts import redirect

# Create your views here.
# views handles http requests


def upload_product(request):
    if request.method == 'POST':
         form = ProductUploadForm(request.POST, request.FILES)
         if form.is_valid():
              form.save()

    else:
         form = ProductUploadForm()

    return render(request, "inventory/product_upload.html", {"form": form})


def products_list(request):
     products = Product.objects.all()
     return render(request, "inventory/products_list.html", {"products": products})

def product_details(request, id):
     products = Product.objects.get(id=id)
     return render(request, "inventory/products_detail.html", {"products": products})


# rendering only works with request from the client
# a http method can be GET, POST, UPDATE, DELETE
# If u dont specify, it automatically GET


# editing data
def edit_product(request, id):
     product = Product.objects.get(id=id)
     if request.method == "POST":
          form = ProductUploadForm(request.POST, instance=product)
          form.is_valid()
          form.save()
          return redirect("product_details_view", id=product.id)


     else: 
          form = ProductUploadForm(instance=product)
          return render(request, "inventory/edit_product.html", {"form":form})