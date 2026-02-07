from django.contrib import admin
from .models import Person,AadharCard

# Register your models here.

class PersonModel(admin.ModelAdmin):
    list_display = ('name','age')

class AadharModel(admin.ModelAdmin):
    list_display = ('person','number')

class AadharModel(admin.ModelAdmin):
    list_display = ('person','number')
    
admin.site.register(Person,PersonModel)
admin.site.register(AadharCard,AadharModel)