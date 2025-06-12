from django.db import models

# Create your models here.

class wydatki(models.Model):
    title = models.CharField(max_length=200)
    amount = models.IntegerField()