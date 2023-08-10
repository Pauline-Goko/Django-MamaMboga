from django.shortcuts import render
from .forms import ReviewViewForm
from .models import Review
from django.shortcuts import redirect

# Create your views here.


def add_review(request):
    if request.method == "POST":
        form = ReviewViewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = ReviewViewForm()
    
    return render(request, "review/review_add.html", {"form": form})


def review_list(request):
    reviews = Review.objects.all()
    return render(request, "review/review_list.html", {"reviews": reviews})



def review_details(request, id):
    review = Review.objects.get(id=id)
    return render(request, "review/review_details.html", {"review": review})


def edit_reviews(request, id):
    review = Review.objects.get(id=id)
    if request.method == "POST":
        form = ReviewViewForm(request.POST, request.FILES)
        form.is_valid()
        form.save()
        return redirect("reviews")
    
    else:
        form = ReviewViewForm(instance=review)
        return render(request, "review/review_edit.html", {"form": form})
    
