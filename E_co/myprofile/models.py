from django.db import models

# Create your models here.
class profile (models.Model):
    profile_id=models.AutoField
    profile_name=models.CharField(max_length=50)
    profile_image=models.CharField(max_length=100)
    profile_date_of_birth=models.DateField()


