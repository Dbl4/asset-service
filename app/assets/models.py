from django.contrib.auth.models import User
from django.db import models


class Asset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    entry_date = models.DateField()
