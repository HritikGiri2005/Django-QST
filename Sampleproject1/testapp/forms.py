from django import forms
from testapp.models import UserProfile

class UserForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields = '__all__'
