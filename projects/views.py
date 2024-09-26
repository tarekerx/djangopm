from django.shortcuts import render
from django.views.generic import ListView,CreateView
from  . import models
from . import forms
from django.urls import reverse_lazy
# Create your views here.



class project_list_view(ListView):
    model = models.Project
    context_object_name = "project_lis"
    template_name = "project/list.html"
    
class project_create_view(CreateView):
    model = models.Project
    form_class = forms.project_create_Form
    template_name = "project/create_project.html"
    success_url = reverse_lazy("project_list")
    