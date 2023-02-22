from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    department = models.CharField(max_length=30)
    class Meta:
        db_table = 'students'