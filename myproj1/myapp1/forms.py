from django import forms
class studentForms(forms.Form):
    firstname=forms.CharField(label="Enter first name",max_length=50)
    Lastname=forms.CharField(label="Enter last name",max_length=50)
    email=forms.EmailField(label="Enter Email")
    file=forms.FileField()