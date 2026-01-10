from django.shortcuts import render
from .models import todo
from django.views.generic import CreateView,DeleteView,UpdateView,ListView

# Create your views here.
class AddTask(CreateView):
    model = todo
    template_name = "create_task.html"
