from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=32)
    age = models.IntegerField()
