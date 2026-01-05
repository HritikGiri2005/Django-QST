from django.contrib import admin
from testapp.models import UserProfile

class User_list(admin.ModelAdmin):
    list_display = ('username','password','about','gender','skills','profile_pic','dob')
admin.site.register(UserProfile,User_list)