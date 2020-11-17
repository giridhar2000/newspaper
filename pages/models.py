from django.db import models

# Create your models here.

class feed(models.Model):
    newsfeed = models.CharField(max_length=500)


