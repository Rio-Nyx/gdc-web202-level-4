from django.shortcuts import render
from django.http import HttpResponseRedirect

pending = []
completed = []


def tasks_view(request):
    return render(request, "tasks.html", {"tasks": pending})


def add_task(request):
    task = request.GET.get("task")
    pending.append(task)
    return HttpResponseRedirect("/tasks")


def complete_task(request, index):
    completed.append(pending.pop(index - 1))
    return HttpResponseRedirect("/tasks")


def delete_task(request, index):
    pending.pop(index - 1)
    return HttpResponseRedirect("/tasks")


def completed_tasks(request):
    return render(request, "allTasks.html", {"completed": completed})


def allTasks(request):
    return render(request, "allTasks.html", {"completed": completed, "tasks": pending})
