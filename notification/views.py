from django.shortcuts import render
from .forms import NotificationForm
from .models import Notification
from django.shortcuts import redirect
# Create your views here.

def add_notification(request):
    if request.method == "POST":
        form = NotificationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = NotificationForm()
    
    return render(request, "notification/notification_add.html", {"form": form})


def notification_list(request):
    notifications = Notification.objects.all()
    return render(request, "notification/notification_list.html", {"notifications": notifications})
   

def notification_details(request, id):
    notification = Notification.objects.get(id=id)
    return render(request, "notification/notification_detail.html", {"notification": notification})


# def notification_edit(request, id):
#     notification = Notification.objects.get(id=id)
#     if request.method == "POST":
#         form = NotificationForm(request.POST, instance=notification)
#         form.is_valid()
#         form.save()
#         return redirect("notification_details", id=notification.id)
        
    
#     else:
#         form = NotificationForm(instance=notification)
#         return render(request, "notification/notification_edit.html", {"form": form})
    


