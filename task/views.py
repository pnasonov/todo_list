from django.shortcuts import render
from django.views.generic import ListView

from task.models import Task, Tag


class TaskListView(ListView):
    model = Task


class TagListView(ListView):
    model = Tag
