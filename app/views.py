from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *
def insert_topic(request):

    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic Insertion is done successfully')

    return render(request,'insert_topic.html')


def insert_webpage(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}

    if request.method=='POST':
        tn=request.POST['tn']
        name=request.POST['name']
        url=request.POST['url'] 
        email=request.POST['email']

        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WO.save() 
        return HttpResponse('Webpage insertion is done successfully')            
    return render(request,'insert_webpage.html',d)



def insert_access(request):
    LOT=Webpage.objects.all()
    d={'webpages':LOT}

    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']
        WO=Webpage.objects.get(name=name)
        AO=Accessrecord.objects.get_or_create(name=WO,author=author,date=date)[0]
        AO.save()
        return HttpResponse('Accessrecord insertion is done Successfully')
    return render(request,'insert_access.html',d)


def retrieve_data(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    if request.method=='POST':
        td=request.POST.getlist('topic')
        print(td)
        webqueryset=Webpage.objects.none()

        for i in td:
            webqueryset=webqueryset|Webpage.objects.filter(topic_name=i)
        d1={'webpages':webqueryset}
        return render(request,'display_webpage.html',d1)
    return render(request,'retrieve_data.html',d)

def checkbox(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'checkbox.html',d)



