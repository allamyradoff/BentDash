from django import forms
from .models import ContactUs



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["email", "name", "message"]
        
        widgets = {
            "email":forms.TextInput(attrs={'class':"form-control", 'placeholder':"email"}),
            "name":forms.TextInput(attrs={'class':"form-control", 'placeholder':"name"}),
            "message":forms.Textarea(attrs={'class':"form-control", 'placeholder':"message"}),
        }

