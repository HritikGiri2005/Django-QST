from django import forms

class ContainerForm(forms.form):
    name = forms.CharField(label='Student Name', max_length=100)
    contact_no = forms.IntegerField(label='Contact Number')