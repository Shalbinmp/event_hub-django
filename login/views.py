from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login
from django.shortcuts import render


# Create your views here.
def add_login(request):
    if request.method=="POST":
        uname=request.POST.get("un")
        passw=request.POST.get("ps")
        obj=Login.objects.filter(username=uname, password=passw)
        tp=""
        for ob in obj:
            tp=ob.type
            uid=ob.u_id
            if tp=="admin":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/admin_home/')
            elif tp=="owner":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/event_home/')
            elif tp=="user":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/user_home/')
        else:
            objlist="username or password incorrect....Please try again....!"
            context={
                'msg':objlist,
            }
        return render(request,'login/login.html',context)
    return render(request,'login/login.html')