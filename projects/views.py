from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from . import models
from . import forms
from django.urls import reverse_lazy, reverse
# Create your views here.


class project_list_view(ListView):
    model = models.Project
    context_object_name = "project_list"
    template_name = "project/list.html"


class project_create_view(CreateView):
    model = models.Project
    form_class = forms.project_create_Form
    template_name = "project/create_project.html"
    success_url = reverse_lazy("project_list")


class project_update_view(UpdateView):
    model = models.Project
    form_class = forms.project_update_form
    template_name = "project/update.html"
    success_url = reverse_lazy("project_list")

    def get_success_url(self) -> str:
        return reverse("project_update", args=[self.object.id])


class task_create_view(CreateView):
    model = models.Task
    fields = ["project", "description"]
    http_method_names = ["post"]

    def get_success_url(self) -> str:
        return reverse("project_update", args=[self.object.project.id])


class tSK_UPDATE_VIEW(UpdateView):
    model = models.Task
    fields = ["is_completed"]
    http_method_names = ["post"]

    def get_success_url(self) -> str:
        return reverse("project_update", args=[self.object.project.id])

class tSK_DELETE_VIEW(DeleteView):
    model = models.Task


    def get_success_url(self) -> str:
        return reverse("project_update", args=[self.object.project.id])
    
class project_delete_view(DeleteView):
    model = models.Project
    template_name = "project/delete.html"
    
    def get_success_url(self) -> str:
        return reverse("project_list")