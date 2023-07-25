
from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    second_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    phone = forms.CharField(max_length=11, min_length=11, required=True)
    message = forms.CharField(widget=forms.Textarea,max_length=500,required=True)