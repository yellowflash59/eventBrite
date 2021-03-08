from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Event
from django.http import JsonResponse

# Create your views here.
def event_add(request):
    print(request.POST)
    if request.method == 'POST' and request.FILES['image']:

        event_name = request.POST['event_name']
        data = request.POST['data']
        location = request.POST['location']

        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        data = Event(event_name=event_name,image=filename,data=data,location=location)
        data.save()


        return redirect('add_events')
    else:
        return render(request,'events.html')

def event_list(request):
    events = Event.objects.all()
    context = {
        # 'is_liked':is_liked,
        'events' : events
    }

    return render(request,'event_list.html',context)

def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Event.objects.get(id = post_id)
        value = ""
        if user in post_obj.is_liked.all():
            post_obj.is_liked.remove(user)
            value = 'Unlike'
        else:
            post_obj.is_liked.add(user)
            value = 'Like'
        
    return redirect('events_list')
