from django.contrib import admin
from .models import todo

# Register your models here.
class todolist(admin.ModelAdmin):
    list_display = ('task_name','date_created')

admin.site.register(todo)
