from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import datetime
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
    image_information = models.CharField(max_length=500,default="")
    image = models.ImageField(upload_to="shop/qrimgs",default="")
    datetime=models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            output = BytesIO()
            img.save(output, format='JPEG', quality=100)
            output.seek(0)
            self.image = InMemoryUploadedFile(
                output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg', output.getbuffer().nbytes, None
            )
        super(qrname, self).save(*args, **kwargs)
