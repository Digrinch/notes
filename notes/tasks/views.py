from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from tasks.models import Task
from tasks.forms import TaskForm

# Create your views here.
def index(request):
    return render(
        request,
        'tasks/index.html',
        {
            'planned': request.user.tasks.filter(status='NS'),
            'worked': request.user.tasks.filter(status='IP'),
            'done': request.user.tasks.filter(status='AD'),
        },
    )

def task_in_work(_request, task_id):
    task = Task.objects.get(pk=task_id)
    task.status = 'IP'
    task.save()
    return HttpResponseRedirect(reverse('tasks:index'))

def task_done(_request, task_id):
    task = Task.objects.get(pk=task_id)
    task.status = 'AD'
    task.save()
    return HttpResponseRedirect(reverse('tasks:index'))

def task_delete(_request, task_id):
    Task.objects.get(pk=task_id).delete()
    return HttpResponseRedirect(reverse('tasks:index'))

def task_create(request):
    form = TaskForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'tasks/create_task.html', {'form': form})
    form.instance.author = request.user
    form.instance.status = 'NS'
    form.save()
    return HttpResponseRedirect(reverse('tasks:index'))

def task_edit(request, task_id):
    form = TaskForm(request.POST or None, instance=Task.objects.get(pk=task_id))
    if not form.is_valid():
        return render(request, 'tasks/create_task.html', {'form': form, 'edit': True})
    form.save()
    return HttpResponseRedirect(reverse('tasks:index'))
