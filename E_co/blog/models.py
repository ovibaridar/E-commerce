from django.db import models

# Create your models here.
class blog_information(models.Model):
    bolg_id=models.AutoField
    blog_hading=models.CharField(max_length=100)
    blog_image=models.CharField(max_length=100)
