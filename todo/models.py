from django.db import models

# Create your models here.


class Todo(models.Model):
    body = models.CharField(max_length=200)
    last_modified = models.DateTimeField(auto_now=True)
