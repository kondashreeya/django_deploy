from django.db import models

# Create your models here.
class employee(models.Model):
    emp_id=models.IntegerField(unique=True)
    emp_name=models.CharField(max_length=20)
    emp_salary=models.FloatField()