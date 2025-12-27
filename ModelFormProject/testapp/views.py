from django.shortcuts import render, HttpResponseRedirect
from testapp.forms import StudentForm
from testapp.models import Student
# Create your views here.

def form_view(request):
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/list")
    else:
        form = StudentForm()
    return render(request,'testapp/studentForm.html',{'form':form})

def stu_list_view(request):
    #how to read records from table
    #Model.object.all()
    stu_list = Student.objects.all()
    return render(request,'testapp/Studentlist.html',{'students':stu_list})

def stu_detail_view(request,id):
    student = Student.objects.get(id=id)
    return render(request,'testapp/Studentdetail.html',{'student':student})

