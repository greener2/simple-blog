import datetime

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=140, null=False, blank=False)
    subtitle = models.CharField(max_length=140, null=False)
    body = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(default=datetime.datetime.utcnow)
