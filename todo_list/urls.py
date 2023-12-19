from django.urls import path

from .views import (home,
                    TaskListView,
                    TaskDetailView,
                    TaskCreateView,
                    TaskUpdateView,
                    TaskDeleteView)


urlpatterns = [
    path("", home, name="home"),
    path("tasks/", TaskListView.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
]
