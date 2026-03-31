from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all().order_by('-created_at')
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('/')
    return render(request, 'home.html', {'tasks': tasks})

def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('/')

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')

