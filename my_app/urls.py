from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects, name="projects"), # otra forma de nombras a las rutas con el name
    path('tasks/<int:id>', views.tasks),
    path('create_task', views.create_task)
]
