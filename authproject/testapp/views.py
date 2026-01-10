from django.shortcuts import render
from django.views.generic import View
# Create your views here.

def view(request):
    return render("navbar.html",name="navbar")

