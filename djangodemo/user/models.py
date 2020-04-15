from django.db import models

# Create your models here.
class User(models.Model):
    no = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=12)
    phone = models.IntegerField(max_length=11)
    account = models.FloatField()
