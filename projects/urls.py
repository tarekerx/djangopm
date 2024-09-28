from django.urls import path
from . import views
urlpatterns = [
    path("", views.project_list_view.as_view(), name="project_list"),
    path("project/create", views.project_create_view.as_view(), name="project_create"),
    path("project/update/<int:pk>",views.project_update_view.as_view(),name="project_update"),
    path("task/create/",views.task_create_view.as_view(),name="task_create"),
    path("task/update/<int:pk>",views.tSK_UPDATE_VIEW.as_view(),name="task_update"),
    path("task/delete/<int:pk>",views.tSK_DELETE_VIEW.as_view(),name="task_delete"),
    path("project/delete/<int:pk>",views.project_delete_view.as_view(),name="project_delete")
]
