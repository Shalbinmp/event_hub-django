from django.shortcuts import render
from feedback.models import Feedback
from owner.models import Owner
import datetime
# Create your views here.
def add_v_fedbck(request):
    obj = Feedback.objects.all()
    context = {
        'x': obj
    }
    return render(request,'feedback/ad_view_feedback.html',context)

def ad_feedback(request):
    ob = Owner.objects.all
    context = {
        'd': ob,
    }
    ss =request.session["u_id"]
    if request.method == 'POST':
        obj = Feedback()
        obj.em_id=request.POST.get('o_id')
        obj.user_id=ss
        obj.feedback=request.POST.get("feedback")
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.save()
    return render(request,'feedback/feedback.html',context)

def view_feedback(request):
    ss = request.session["u_id"]
    obj = Feedback.objects.filter(feedback_id=ss)
    context = {
        'y': obj
    }
    return render(request,'feedback/view_feedback(owner).html',context)