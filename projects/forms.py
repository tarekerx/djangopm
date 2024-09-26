from django import forms
from .models import *

class project_create_Form(forms.ModelForm):

    class Meta:
        model = Project
        fields = ("category","title","description")
        widgets = {
            "category":forms.Select(),
            "title":forms.TextInput(),
            "description":forms.Textarea()
        }



