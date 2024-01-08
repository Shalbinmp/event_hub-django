from django.shortcuts import render
from facilities.models import Facilities
from event.models import Event

# Create your views here.
def ad_view_facilities(request):
    obj = Facilities.objects.all()
    context = {
        'x': obj
    }
    return render(request,'facilities/ad_view_facilities.html',context)

def ad_facility(request):
    ob = Event.objects.all
    context = {
        'd': ob,
    }
    ss =request.session["u_id"]
    if request.method == 'POST':
        obj = Facilities()
        obj.event_id=request.POST.get('event_id')
        obj.em_id=ss
        obj.description=request.POST.get("description")
        obj.amount=request.POST.get("amount")
        obj.type=request.POST.get("type")
        obj.save()
    return render(request,'facilities/facility.html',context)

def v_faclities(request):
    obj = Facilities.objects.all()
    context = {
        'y': obj
    }
    return render(request,'facilities/view_facilities.html',context)