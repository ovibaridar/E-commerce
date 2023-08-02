# models.py
from django.db import models

class SketchImage(models.Model):
    image = models.ImageField(upload_to='sketch_images/', blank=True, null=True)

    def __str__(self):
        return f'SketchImage {self.id}'
