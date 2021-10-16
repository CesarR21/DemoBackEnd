from django.db import models


# Create your models here.
class Budget(models.Model):
    balance = models.IntegerField()
    Income = models.IntegerField()
    expense =models.IntegerField()
    date = models.DateField(max_length=500)
    category=models.CharField(max_length=500)
    amount =models.IntegerField()
    
    spent=models.IntegerField()