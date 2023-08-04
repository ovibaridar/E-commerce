from django.contrib import admin

# Register your models here.

from .models import product
from .models import qrname
from .models import school_addmission


admin.site.register(product)
admin.site.register(qrname)
admin.site.register(school_addmission)