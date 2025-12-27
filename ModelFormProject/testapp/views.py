from django.shortcuts import render
from testapp.forms import StudentForm
# Create your views here.

def StudentForm(request):
    form = StudentForm()
    return render(request,'testapp/studentForm.html')
