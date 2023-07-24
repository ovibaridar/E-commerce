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

class qrname(models.Model):
    Qrname_id=models.AutoField
    name = models.CharField(max_length=100,default="")
    second_name = models.CharField(max_length=100,default="")
    email = models.CharField(max_length=100,default="")
    phone = models.CharField(max_length=100,default="")
    image = models.ImageField(upload_to="shop/qrimgs",default="")

    def __str__(self):
        return self.name