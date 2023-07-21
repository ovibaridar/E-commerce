from django.shortcuts import render
from django.http import HttpResponseGone
from .models import product
# Create your views here.
def shophome(reuest):

    all_products = product.objects.all()

    # return HttpResponseGone ("gu")
    return render(reuest,'shop/hello.html', {'products': all_products})







