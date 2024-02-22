from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    title = 'Welcome to my App'
    return render(request, 'index.html', { 'title': title })

def hello(request, username):
    return HttpResponse('Hello %s' % username)

def projects(request):
    records = list(Project.objects.values())
    return JsonResponse(records, safe=False)

def tasks(request, id):
    # task = Task.objects.get(id=id)
    # Below ins the same than above
    task = get_object_or_404(Task, id=id)
    return JsonResponse('Task: %s' % task.title, safe=False)
