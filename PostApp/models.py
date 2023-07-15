from django.db import models


class Post(models.Model):
    username = models.CharField(max_length=30)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=500)
