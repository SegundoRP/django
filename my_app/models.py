from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    """ method for show name of model in admin panel instead object """
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # CASCADE delete tasks associated to a parent if it is deleted
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.project.name
