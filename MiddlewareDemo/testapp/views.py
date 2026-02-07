from django.shortcuts import render

# Create your views here.
def hello_view(request):
    print('View is executed')
    return render(request,'testapp/home.html')