from django.http import HttpResponse
from django.urls import reverse, path
from django.shortcuts import get_object_or_404, render
from .models import Project, Task
from quality_control.views import index as quality_index


def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/projects_list.html', {'projects_list': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'tasks/project_detail.html', {'project' : project})

def task_detail(request, project_id, task_id):
    task = get_object_or_404(Task, id=task_id, project=project_id)
    return render(request, 'tasks/task_detail.html', {'task' : task})

def index(request):
    return render(request, 'tasks/index.html')
