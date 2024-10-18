from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


class project_list_view(LoginRequiredMixin, ListView):
    model = models.Project
    context_object_name = "project_list"
    template_name = "project/list.html"
    paginate_by = 6

    def get_queryset(self):
        query_set = super().get_queryset()
        where = {"user_id": self.request.user}
        q = self.request.GET.get("q", None)
        if q:
            where["title__icontains"] = q
        return query_set.filter(**where)


class project_create_view(LoginRequiredMixin, CreateView):
    model = models.Project
    form_class = forms.project_create_Form
    template_name = "project/create_project.html"
    success_url = reverse_lazy("project_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class project_update_view(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Project
    form_class = forms.project_update_form
    template_name = "project/update.html"
    success_url = reverse_lazy("project_list")

    def test_func(self):
        return self.get_object().user_id == self.request.user.id

    def get_success_url(self) -> str:
        return reverse("project_update", args=[self.object.id])


class task_create_view(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.Task
    fields = ["project", "description"]
    http_method_names = ["post"]

    def test_func(self):
        project_id = self.request.POST.get("project", "")

        return models.Project.objects.get(pk=project_id).user_id == self.request.user.id

    def get_success_url(self) -> str:
        return reverse("project_update", args=[self.object.project.id])


class tSK_UPDATE_VIEW(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Task
    fields = ["is_completed"]
    http_method_names = ["post"]

    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id

    def get_success_url(self) -> str:
        return reverse("project_update", args=[self.object.project.id])


class tSK_DELETE_VIEW(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Task

    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id

    def get_success_url(self) -> str:
        return reverse("project_update", args=[self.object.project.id])


class project_delete_view(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Project
    template_name = "project/delete.html"

    def test_func(self):
        return self.get_object().user_id == self.request.user.id

    def get_success_url(self) -> str:
        return reverse("project_list")
