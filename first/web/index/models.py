
from django.db import models


# Create your models here.
class classform(models.Model):
    Name=models.CharField(max_length=30)
    StuID=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    Mon=models.TextField()
    Tue=models.TextField()
    Wed=models.TextField()
    Thu=models.TextField()
    Fri=models.TextField()
    
    def __str__(self):
        return self.Name

class classform2(models.Model):
    Name=models.CharField(max_length=30)
    StuID=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    Mon=models.TextField()
    Tue=models.TextField()
    Wed=models.TextField()
    Thu=models.TextField()
    Fri=models.TextField()
    
    def __str__(self):
        return self.Name