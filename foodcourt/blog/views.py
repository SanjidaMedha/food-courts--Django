from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def home(req):
    return render(req,'home.html')

def about(req):
    return render(req,'about.html')

def roti(req):
    return render(req,'roti.html')

def coconut(req):
    return render(req,'coconut.html')

def biryani(req):
    return render(req,'biryani.html')

def fruits(req):
    return render(req,'fruits.html')