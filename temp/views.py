from django.shortcuts import render
from event.models import Event
# Create your views here.


def admin_home(request):
    return render(request,'temp/admin.html')



def Event_home(request):
    return render(request,'temp/event manager.html')


def user_home(request):
    return render(request,'temp/user.html')


def main_home(request):
    return render(request,'temp/index.html')


def view_event_m(request):
    return render(request,'temp/view_templates_event.html')


def view_admin(request):
    return render(request,'temp/view_templates_admin.html')


def view_user(request):
    return render(request,'temp/view_templates_user.html')


def add_event(request):
    obj=Event.objects.all()
    context={
        'x':obj
    }
    return render(request,'temp/user.html',context)