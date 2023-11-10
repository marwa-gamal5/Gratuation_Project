
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.

def home(request):
    return render(request, 'home.html')
def abo(request):
    return render(request, 'about.html')
def res(request):
    return render(request,'reaserch.html')