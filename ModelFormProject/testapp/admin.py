from django.contrib import admin
from testapp.models import Student

# Register your models here.
class stu_list(admin.ModelAdmin):
    list_display = ('first_name','last_name','enrollment_number')
admin.site.register(Student,stu_list)