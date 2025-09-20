from django.shortcuts import render
from tasks.models import Task

# Create your views here.

def index(request):
    tasks = Task.objects.all()

    return render(request, "./core/index.html", {'tasks': tasks})

def all_tasks(request):
    tasks = Task.objects.all()

    return render(request, "./core/all_tasks.html", {'tasks': tasks})