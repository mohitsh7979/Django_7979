from django import forms

class shopingform(forms.Form):
    name=forms.CharField(max_length=10)
    password=forms.CharField(max_length=10)