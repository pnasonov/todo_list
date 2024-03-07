from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, View

from task.models import Task, Tag


class TaskListView(ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags").order_by(
        "done", "-created_at"
    )


class TagListView(ListView):
    model = Tag


class DoneTask(View):
    def post(self, request, pk) -> HttpResponseRedirect:
        task = get_object_or_404(Task, pk=pk)
        task.done = not task.done
        task.save()
        return redirect("task:task-list")
