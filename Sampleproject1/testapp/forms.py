from django import forms
from .models import UserProfile

class UserProfile(forms.ModelForm):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect
    )

    profile_pic = forms.ImageField(
        label='Upload Profile Picture',
        widget=forms.ClearableFileInput(attrs={
            'accept': 'image/*'
        })
    )

    class Meta:
        model = UserProfile
        fields = "__all__"

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter username'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Enter password'
            }),
            'about': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Tell something about yourself'
            }),
            'skills': forms.TextInput(attrs={
                'placeholder': 'e.g. Python, Django'
            }),
            'dob': forms.DateInput(attrs={
                'type': 'date'
            }),
        }
