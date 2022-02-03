from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

current_tasks = []
completed_tasks = []

def task_view(request):
  return render(request, "tasks.html", { "tasks": current_tasks})

def add_task_view(request):
  current_tasks.append(request.GET.get("task"))
  return HttpResponseRedirect("/tasks")

def delete_task_view(request, index):
  del current_tasks[index -1]
  return HttpResponseRedirect("/tasks")

def completed_tasks_view(request):
  return render(request, "completed.html", { "tasks": completed_tasks})

def complete_task_view(request, index):
  item = current_tasks.pop(index-1)
  completed_tasks.append(item)
  return HttpResponseRedirect("/tasks")

def all_tasks_view(request):
  return render(request, "all_tasks.html", {"current": current_tasks, "completed": completed_tasks})