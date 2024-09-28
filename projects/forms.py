from django import forms
from .models import *


class project_create_Form(forms.ModelForm):

    class Meta:
        model = Project
        fields = ("category", "title", "description")
        widgets = {
            "category": forms.Select(),
            "title": forms.TextInput(),
            "description": forms.Textarea()
        }


class project_update_form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("category", "title", "status")
        widgets = {
            "category": forms.Select(),
            "title": forms.TextInput(),
            "status": forms.Select()
        }
