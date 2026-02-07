from django.contrib import admin
from .models import Person,AadharCard,Father,Children

# Register your models here.

class PersonModel(admin.ModelAdmin):
    list_display = ('name','age')

class AadharModel(admin.ModelAdmin):
    list_display = ('person','number')

class FatherModel(admin.ModelAdmin):
    list_display = ('name',)

class ChildrenModel(admin.ModelAdmin):
    list_display = ('father','child_name')

admin.site.register(Person,PersonModel)
admin.site.register(AadharCard,AadharModel)
admin.site.register(Father,FatherModel)
admin.site.register(Children,ChildrenModel)
