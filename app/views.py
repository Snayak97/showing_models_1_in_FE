from django.shortcuts import render

from django.db.models.functions import Length #using lenth function

from app.models import *

from django.db.models import Q #using Q object for concatination
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
    # webpages=Webpage.objects.all()
    # webpages=Webpage.objects.filter(name__startswith='V')
    webpages=Webpage.objects.filter(url__startswith='http')
    webpages=Webpage.objects.filter(name__endswith='i')
    webpages=Webpage.objects.filter(url__contains='.com')
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(Q(name='Soumya') | Q(url='http:'))
    webpages=Webpage.objects.filter(Q(name='Soumya') & Q(url='http://Soumya.com'))


    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)

#display AccessRecord Models

def display_AcessRecord(request):
    Acess=AcessRecord.objects.all()
    Acess=AcessRecord.objects.filter(date='2023-06-05')
    Acess=AcessRecord.objects.filter(date__gt='2023-06-05')
    Acess=AcessRecord.objects.filter(date__gte='2023-06-05')
    Acess=AcessRecord.objects.filter(date__lt='2023-06-05')
    Acess=AcessRecord.objects.filter(date__lte='2023-06-05')
    Acess=AcessRecord.objects.filter(date__day__gte='05')
    Acess=AcessRecord.objects.filter(date__year__lte='2023')
    Acess=AcessRecord.objects.filter(date__month__lt='05')
    Acess=AcessRecord.objects.all()


    d={'Acess':Acess}
    return render(request,'display_AcessRecord.html',d)



def update_webpage(request):
    # using update method
    # Webpage.objects.filter(name='Soumya').update(url='https://SN.in')#single row certified then upadate
    # Webpage.objects.filter(topic_name='Cricket').update(url='https://bcci.in') # ifmultiple row certisfied its update
    # Webpage.objects.filter(topic_name='Cricket msd').update(url='https://bcci.in') #if Zero row certisfied not affected
    # Webpage.objects.filter(topic_name='Cricket').update(url='https://bcci.in') #while fk column update we use value which is present in table

# using update or create method
    # Webpage.objects.update_or_create(name='Soumya',defaults={'url':'http://soumya.in'})#single row certified then upadate
    # Webpage.objects.update_or_create(topic_name='Cricket',defaults={'url':'http://soumya.in'})#if multiple row certified it through error
    # Webpage.objects.update_or_create(topic_name='Chess',defaults={'url':'http://s.in'})
    CTO=Topic.objects.get(topic_name='Cricket')
    Webpage.objects.update_or_create(name='pdya',defaults={'topic_name': CTO,})
    #Webpage.objects.update_or_create(name='pandya',defaults={'topic_name': CTO,'url':'https://pandya.in'})#while fk column update we should provide objects which is present in table


    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)


#delete the data
def delete_webpage(request):
    Webpage.objects.filter(name='pdya').delete()


    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)



