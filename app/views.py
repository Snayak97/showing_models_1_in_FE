from django.shortcuts import render

from django.db.models.functions import Length

from app.models import *
# create new views for font end


#display Topic Models

def display_topic(request):
    topics=Topic.objects.all()
    topics=Topic.objects.all().order_by('-topic_name')#desending order
    topics=Topic.objects.all().order_by(Length('topic_name').desc())#lenthwise
    topics=Topic.objects.all()[1:3:]#how many row we want
    topics=Topic.objects.exclude(topic_name='Cricket')#except condition all record given
    d={'topics':topics}
    return render(request,'display_topic.html',d)

#display Webpage Models

def display_webpage(request):
    webpages=Webpage.objects.filter(topic_name='Cricket')
    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)

#display AccessRecord Models

def display_AcessRecord(request):
    Acess=AcessRecord.objects.all()
    d={'Acess':Acess}
    return render(request,'display_AcessRecord.html',d)




