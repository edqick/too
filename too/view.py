#-*- coding:utf-8 -*-
'''
Created on 2017年8月27日

@author: qick
'''
#from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
context = {    'home':'index.html',
               'album':'index-1.html',
               'network':'index-2.html',
               'blog':'index-3.html',
               'contact':'index-4.html',
               'test':'test.html'}
def index(request):
    return render(request,context['home'], {'context':context})

def album(request):
    return render(request,context['album'], {'context':context})

def network(request):
    return render(request,context['network'], {'context':context})

def blog(request):
    return render(request,context['blog'], {'context':context})

def contact(request):
    return render(request,context['contact'], {'context':context})

def test(request):
    return render(request,context['test'], {'context':context})

def admin(request):
    return HttpResponse("You're looking at question ." )

def hello(request):
    #return HttpResponse("Hello world ! ")
    context          = {}
    context['num'] = range(10)
    return render(request, 'hello.html', context)