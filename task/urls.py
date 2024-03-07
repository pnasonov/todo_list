from django.urls import path
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from task.models import Task, Tag
from task.views import TaskListView, DoneTask, TagListView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path(
        "task/create/",
        CreateView.as_view(model=Task, fields="__all__", success_url="/"),
        name="task-create",
    ),
    path(
        "task/<int:pk>/update/",
        UpdateView.as_view(model=Task, fields="__all__", success_url="/"),
        name="task-update",
    ),
    path(
        "task/<int:pk>/delete/",
        DeleteView.as_view(model=Task, success_url="/"),
        name="task-delete",
    ),
    path("task/<int:pk>/done/", DoneTask.as_view(), name="done"),
    path("tag/", TagListView.as_view(), name="tag-list"),
    path(
        "tag/create/",
        CreateView.as_view(model=Tag, fields="__all__", success_url="/tag"),
        name="tag-create",
    ),
    path(
        "tag/<int:pk>/update/",
        UpdateView.as_view(model=Tag, fields="__all__", success_url="/tag"),
        name="tag-update",
    ),
    path(
        "tag/<int:pk>/delete/",
        DeleteView.as_view(model=Tag, success_url="/tag"),
        name="tag-delete",
    ),
]

app_name = "task"
