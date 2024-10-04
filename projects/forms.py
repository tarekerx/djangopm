from django import forms
from .models import *

attrs = {"class": "form-control"}
class project_create_Form(forms.ModelForm):

    class Meta:
        model = Project
        fields = ("category", "title", "description")
        widgets = {
            "category": forms.Select(attrs=attrs),
            "title": forms.TextInput(attrs=attrs),
            "description": forms.Textarea(attrs=attrs)
        }


class project_update_form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("category", "title", "status")
        widgets = {
            "category": forms.Select(attrs=attrs),
            "title": forms.TextInput(attrs=attrs),
            "status": forms.Select(attrs=attrs)
        }
