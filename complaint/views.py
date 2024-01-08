from django.shortcuts import render
from complaint.models import Complaint
import datetime
from user.models import User
from owner.models import Owner
# Create your views here.

def ad_v_post_rply(request):
    obj=Complaint.objects.all()
    context={
        'x':obj
    }
    return render(request,'complaint/ad_view &post_reply.html',context)

def add_complaint(request):
    # ob = User.objects.all()
    obbb = Owner.objects.all()
    context = {
        # 'a': ob,
        'd': obbb,
    }
    ss =request.session["u_id"]
    if request.method == 'POST':
        obj = Complaint()
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.complaint=request.POST.get("complaint")
        obj.user_id=ss
        obj.em_id=request.POST.get('o_id')
        obj.replay='pending'
        obj.save()
    return render(request,'complaint/Complaint.html',context)

def add_reply_view(request):
    obj=Complaint.objects.all()
    context={
        'x':obj
    }
    return render(request,'complaint/replay_view.html',context)

def add_view_cmplnt(request):
    obj = Complaint.objects.all()
    context = {
        'y': obj
    }
    return render(request,'complaint/view_complaint.html',context)

def ad_v_rply(request):
    ss = request.session["u_id"]
    obj = Complaint.objects.filter(complaint_id=ss)
    context = {
        'z': obj
    }
    return render(request, 'complaint/view_reply_owner.html', context)




def ad_reply(request,idd):
    if request.method == 'POST':
        obj = Complaint.objects.get(complaint_id=idd)
        obj.reply=request.POST.get('reply')
        obj.save()
        return ad_v_post_rply(request)
    return render(request,'complaint/add_reply.html')