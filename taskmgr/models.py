from django.db import models

# Create your models here.

STATUS_TYPE = ['completed', 'not completed', 'in progress']


class Task(models.Model):
    # __tablename__ = 'tasks'
    title = models.CharField(max_length=255)
    text = models.TextField()
    status = models.CharField(max_length=100, choices=[
                              (s, s) for s in STATUS_TYPE])
