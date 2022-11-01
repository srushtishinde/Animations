from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Animation(models.Model):
    username = models.CharField(max_length=256)
    editor = models.CharField(max_length=256)
    editor1 = models.CharField(max_length=256)
    file01 = models.FileField(null=True)
    type = models.CharField(max_length=256)
    aname = models.CharField(max_length=256)

