from django.shortcuts import render
from django.http import HttpResponse

context = {    'home':'index.html',
               'album':'index-1.html',
               'network':'index-2.html',
               'blog':'index-3.html',
               'contact':'index-4.html',
               'login':'login.html'}
def index(request):
    import os
    pathDir =  os.listdir('./static/images/city/')
    citys = {}
    for allDir in pathDir:
        child = allDir.split('.')
        citys[child[0]] = allDir
    #print(citys)
    #context['citys'] = citys
    #print(context['citys'])
    return render(request,context['home'], {'citys':citys})

def album(request):
    return render(request,context['album'], {'context':context})

def network(request):
    return render(request,context['network'], {'context':context})

def blog(request):
    return render(request,context['blog'], {'context':context})

def contact(request):
    return render(request,context['contact'], {'context':context})
