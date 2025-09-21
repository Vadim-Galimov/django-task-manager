from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import Task
from tasks.forms import TaskCreateForm

# Create your views here.

def index(request):
    tasks = Task.objects.all()

    return render(request, "./core/index.html", {'tasks': tasks})

def all_tasks(request):
    tasks = Task.objects.all()

    return render(request, "./core/all_tasks.html", {'tasks': tasks})

def add_task(request):


    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_tasks')
    else:
        form = TaskCreateForm()

    return render(request, "./core/add_task.html", {'form': form})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('all_tasks')
