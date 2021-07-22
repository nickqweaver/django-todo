from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    body = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.body