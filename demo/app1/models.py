from django.db import models

class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=50)
    esalary = models.FloatField() 

    def __str__(self):
        return f"{self.eid}--{self.ename}"
