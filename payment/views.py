from django.shortcuts import render
from payment.models import Payment
from booking.models import Booking
import datetime
# Create your views here.
def ad_v_payment(request):
    obj = Payment.objects.all()
    context = {
        'x': obj
    }
    return render(request,'payment/AD_VIEW_payments.html',context)

def ad_owner_v_paymnt(request):
    ss = request.session["u_id"]
    obj = Payment.objects.filter(pay_id=ss)
    context = {
        'y': obj
    }
    return render(request,'payment/owner_view payment.html',context)

def ad_paymnt(request,idd):
    obb=Booking.objects.get(booking_id=idd)
    context={
        'x':obb
    }
    ss =request.session["u_id"]
    if request.method == 'POST':
        obj = Payment()
        obj.booking_id=idd
        obj.user_id=ss
        obj.cardholder_name=request.POST.get("cardholder")
        obj.cvv=request.POST.get("cvv")
        obj.account_no=request.POST.get("acno")
        obj.amount=request.POST.get("amount")
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.em_id=1
        obj.status='paid'
        obj.save()
    return render(request,'payment/payment.html',context)

def ad_veiw_paymnt(request):
    obj = Payment.objects.all()
    context = {
        'z': obj
    }
    return render(request,'payment/view_payment(owner).html',context)

