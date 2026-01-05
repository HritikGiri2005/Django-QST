from django.shortcuts import render,HttpResponseRedirect
from .models import UserProfile
from .forms import UserProfileForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserProfileForm()
    return render(request,'testapp/register.html',{'form':form})

def success(request):
    users = UserProfile.objects.all()
    return render(request, 'testapp/success.html', {'users': users})

def profileview(request,id):
    view = UserProfile.objects.all().get(id=id)
    return render(request,'testapp/view.html',{'view':view})
