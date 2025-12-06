from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_view(request):
    message = """"
    <h1 style = "color">
        Hello! my name is <span>Hritik</span>
    </h1>
    """

    return HttpResponse(message)
