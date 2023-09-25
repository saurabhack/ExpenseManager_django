from django.db import models
from datetime import datetime
# Create your models here.
class Expenses(models.Model):
    description=models.CharField(max_length=100)
    Amount=models.IntegerField()
    date= models.DateField(default=None, null=True, blank=True)
