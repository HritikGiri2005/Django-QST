from django.shortcuts import render
from .models import todo
from django.views.generic import CreateView,DeleteView,UpdateView,ListView

# Create your views here.
class AddTask(CreateView):
    model = todo
    fields = '__all__'
    template_name = "testapp/create_task.html"
    success_url = "/home/"

class home(ListView):
    model = todo
    template_name = "testapp/home.html"

c
