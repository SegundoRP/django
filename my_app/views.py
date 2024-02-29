from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask

# Create your views here.
def index(request):
    title = 'Welcome to my App'
    return render(request, 'index.html', { 'title': title })

def hello(request, username):
    return HttpResponse('Hello %s' % username)

def projects(request):
    # records = list(Project.objects.values())
    # return JsonResponse(records, safe=False)
    projects_objects = Project.objects.all()
    return render(request, 'projects.html', { 'projects': projects_objects })

def tasks(request, id):
    # task = Task.objects.get(id=id)
    # Below ins the same than above
    task = get_object_or_404(Task, id=id)
    return JsonResponse('Task: %s' % task.title, safe=False)

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', { 'form': CreateNewTask() })
    else:
        Task.objects.create(title=request.POST['title'],
        description=request.POST['description'], project_id=2)
        return redirect('/projects/')
