from django.shortcuts import render
from event.models import Event
from django.core.files.storage import FileSystemStorage

# from e
# Create your views here.
def add_view_events(request):
    obj = Event.objects.all()
    context = {
        'x': obj
    }
    return render(request,'event/ad_view_events.html',context)

def add_event(request):
    ss = request.session["u_id"]
    if request.method == 'POST':
        obj = Event()
        obj.em_id=ss
        obj.name=request.POST.get("name")
        obj.type=request.POST.get("text")
        # obj.photo=request.POST.get("choose_file")
        myfile=request.FILES['choose_file']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.image=myfile.name
        obj.amount=request.POST.get('am')
        obj.save()
    return render(request,'event/event.html')

def user_v_event(request,idd):
    obj = Event.objects.filter(em_id=idd)
    context = {
        'y': obj
    }
    return render(request,'event/sample.html',context)