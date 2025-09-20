from django.shortcuts import render
from tasks.models import Task

# Create your views here.

def index(request):
    tasks = Task.objects.all()

    return render(request, "./core/index.html", {'tasks': tasks})