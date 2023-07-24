from django.db import models

class chakedb(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=20,default="")
    age=models.CharField(max_length=20,default="")
# Create your models here.
    def __str__(self):
        return self.name