from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    user = ForeignKey(User, on_delete=models.CASCADE)

class Audit(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=255, blank=True, null=True)
