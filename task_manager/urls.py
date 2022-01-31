from django.contrib import admin
from django.urls import path
import tasks.views as views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.allTasks),
    path("tasks/", views.tasks_view),
    path("completed_tasks/", views.completed_tasks),
    path("add-task/", views.add_task),
    path("delete-task/<int:index>/", views.delete_task),
    path("complete_task/<int:index>/", views.complete_task),
    path("all_tasks/", views.allTasks),
]
