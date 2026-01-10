from django.shortcuts import render
from django.views.generic import View
# Create your views here.

def nav(request):
    return render(request,"navbar.html")

