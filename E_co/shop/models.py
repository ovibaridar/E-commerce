from django.db import models

# Create your models here.
class product(models.Model):

    products_id=models.AutoField
    products_name=models.CharField(max_length=30)

    catagory=models.CharField(max_length=30,default="")
    sub_catagory=models.CharField(max_length=30,default="")
    price=models.CharField(max_length=30,default=0)
    image=models.ImageField(upload_to="shop/imges",default="")
    products_information=models.CharField(max_length=300)
    products_date=models.DateField

    def __str__(self):
        return self.products_name
