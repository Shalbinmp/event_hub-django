from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from owner.models import Owner
from login.models import Login

# Create your views here.
def ad_mng_owner(request):
    obj = Owner.objects.all()
    context = {
        'x': obj
    }
    return render(request,'owner/ad_mng_owner.html',context)

def ad_eventmngr(request):
    if request.method == 'POST':
        obj = Owner()
        obj.name=request.POST.get("name")
        obj.password=request.POST.get("password")
        obj.phone=request.POST.get("phone")
        obj.address=request.POST.get("address")
        obj.emailid=request.POST.get("email")
        # obj.license=request.POST.get("choose file")
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.license = myfile.name

        # obj.image=request.POST.get('img')
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.image = myfile.name

        obj.status='pending'
        obj.save()

        obj1 = Login()
        obj1.username = obj.name
        obj1.password = obj.password
        obj1.type = "owner"
        obj1.u_id = obj.em_id
        obj1.save()

    return render(request,'owner/eventmanager.html')


def apprv(request,idd):
    obj=Owner.objects.get(em_id=idd)
    obj.status='Approved'
    obj.save()
    return ad_mng_owner(request)

def rjct(request,idd):
    obj=Owner.objects.get(em_id=idd)
    obj.status='Reject'
    obj.save()
    return ad_mng_owner(request)



def vw_audi(request):
    obj = Owner.objects.all()
    context = {
        'j': obj
    }
    return render(request,'owner/sample.html',context)


def mng_profile(request):
    ss=request.session["u_id"]
    obj = Owner.objects.filter(em_id=ss)
    context = {
        'k': obj
    }
    return render(request,'owner/profile_mng.html',context)



def edit(request,idd):
    obb=Owner.objects.get(em_id=idd)
    context={
        'f':obb
    }
    if request.method == 'POST':
        obj = Owner.objects.get(em_id=idd)
        obj.name=request.POST.get("name")
        obj.password=request.POST.get("password")
        obj.phone=request.POST.get("phone")
        obj.address=request.POST.get("address")
        obj.emailid=request.POST.get("email")
        # obj.license=request.POST.get("choose file")
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.license = myfile.name

        # obj.image=request.POST.get('img')
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.image = myfile.name

        obj.status='pending'
        obj.save()
        return mng_profile(request)

        # obj1 = Login.objects.get(u_id=idd)
        # obj1.username = obj.name
        # obj1.password = obj.password
        # obj1.type = "owner"
        # obj1.u_id = obj.em_id
        # obj1.save()

    return render(request,'owner/edit.html',context)


def delete(request,idd):
    obj=Owner.objects.get(em_id=idd)
    obj.delete()
    return mng_profile(request)


