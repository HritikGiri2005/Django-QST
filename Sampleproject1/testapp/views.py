from django.shortcuts import render
from .models import UserProfile
from .forms import UserProfile

# Create your views here.

def register(request):
    form = UserProfile()
    return render(request, 'testapp/register.html', {'form': form})

def success(request):
    return render(request,'testapp/success.html')
