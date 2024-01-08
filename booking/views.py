
from django.shortcuts import render
from booking.models import Booking
from user.models import User
from facilities.models import Facilities
from event.models import Event
from owner.models import Owner
# Create your views here.

def ad_bkg(request,idd):
    ob = Event.objects.get(event_id=idd)
    obb = Facilities.objects.all
    obbb = Owner.objects.all()
    context = {
        'a': ob,
        's': obb,
        'd': obbb,
    }
    ss = request.session["u_id"]
    if request.method == 'POST':
        obj = Booking()
        obj.user_id = ss
        obj.facility_id =request.POST.get('f_id')
        obj.em_id=request.POST.get('cz')
        obj.event_id=idd
        k = obj.facility.amount
        b = obj.event.amount
        obj.amount = (int(b) + int(k))
        obj.date = request.POST.get('date')
        obj.time = request.POST.get('time')
        obj.status ='pending'
        obj.save()

    return render(request,'booking/Booking.html', context)

def ad_view_mng_bkg(request):
    ss = request.session["u_id"]
    obj = Booking.objects.filter(em_id=ss)
    context = {
        'x': obj
    }
    return render(request, 'booking/view_and_manage_booking(owner).html', context)

def apprv(request,idd):
    obj=Booking.objects.get(booking_id=idd)
    obj.status='Approved'
    obj.save()
    return ad_view_mng_bkg(request)


def reject(request,idd):
    obj=Booking.objects.get(booking_id=idd)
    obj.status='reject'
    obj.save()
    return ad_view_mng_bkg(request)

def manage(request):
    ss=request.session["u_id"]
    obj = Booking.objects.filter(status="Approved",user_id=ss)
    context = {
        'y': obj
    }
    return render(request, 'booking/view approved booking and pay.html', context)