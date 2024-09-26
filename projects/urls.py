from django.urls import path
from . import views
urlpatterns = [
    path("", views.project_list_view.as_view(), name="project_list"),
    path("project/create", views.project_create_view.as_view(), name="project_create")
]
