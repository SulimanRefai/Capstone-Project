from django.db import models
from django.contrib.auth.models import User

class Calendar(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
