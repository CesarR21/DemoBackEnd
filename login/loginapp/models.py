from django.db import models

# Create your models here.
class Login(models.Model):
    user_name = models.CharField(max_length=500)
    password=models.CharField(max_length=500)