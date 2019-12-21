from django import forms
from .models import formModel
class DataForm(forms.Form):
    name=forms.CharField(max_length=100)
    adress=forms.CharField(max_length=100)
    phno=forms.IntegerField()
class modelform(forms.ModelForm):
    class Meta:
        model=formModel
        fields=('name','body')
