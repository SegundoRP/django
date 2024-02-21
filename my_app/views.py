from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Index page')

def hello(request, username):
    return HttpResponse('Hello %s' % username)
