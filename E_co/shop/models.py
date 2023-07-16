from django.db import models

# Create your models here.
class product(models.Model):

    products_id=models.AutoField
    products_name=models.CharField(max_length=30)
    products_information=models.CharField(max_length=300)
    products_date=models.DateField