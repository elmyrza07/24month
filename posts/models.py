from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    rate = models.IntegerField(null = True)
    is_active = models.BooleanField(default=True)