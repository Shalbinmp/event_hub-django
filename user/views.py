from django.shortcuts import render
from user.models import User
from login.models import Login
def add_userreg(request):
    if request.method == 'POST':
        obj = User()
        obj.address = request.POST.get("addr")
        obj.name = request.POST.get("name")
        obj.phone = request.POST.get("number")
        obj.email = request.POST.get("email")
        obj.password = request.POST.get("password")
        obj.save()

        obj1 = Login()
        obj1.username = obj.name
        obj1.password = obj.password
        obj1.type = "user"
        obj1.u_id = obj.user_id
        obj1.save()
    return render(request,'user/userreg.html')

def view_user(request):
    obj=User.objects.all()
    context={
        'x':obj
    }
    return render(request, 'user/view_user.html',context)
# Create your views here.
