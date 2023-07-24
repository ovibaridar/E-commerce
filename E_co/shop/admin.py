from django.contrib import admin

# Register your models here.

from .models import product
from .models import qrname

admin.site.register(product)
admin.site.register(qrname)