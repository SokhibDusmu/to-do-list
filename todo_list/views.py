from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)


from .models import Task


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "todo_list/home.html")


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context['tasks'].filter(user=self.request.user)
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"

    def get_queryset(self):
        base_qs = super(TaskDetailView, self).get_queryset()
        return base_qs.filter(user=self.request.user)  


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Task created! Urrraaa")
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy("tasks")

    def get_queryset(self):
        base_qs = super(TaskUpdateView, self).get_queryset()
        return base_qs.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Task updated! Urrraaa :)")
        return super(TaskUpdateView, self).form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")

    def get_queryset(self):
        base_qs = super(TaskDeleteView, self).get_queryset()
        return base_qs.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Task deleted! :(")
        return super(TaskDeleteView, self).form_valid(form)
