from django.shortcuts import render;
from django.http import HttpResponse

#Create your views here...
def f1(request):
        return HttpResponse("<h1>Hello From DemoApp1 f1()</h1><hr />");
def f2(request):
        return HttpResponse("<h2>Hello From DemoApp2 f2()</h2><hr />");    