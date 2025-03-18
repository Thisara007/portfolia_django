from django import forms
from .models import contact

class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields="__all__"
        
        labels={}
    
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "msg":forms.Textarea(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "mobile":forms.TextInput(attrs={"class":"form-control"})
        }