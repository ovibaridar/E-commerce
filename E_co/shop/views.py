from django.shortcuts import render
from django.http import HttpResponseGone

# Create your views here.
def shophome(reuest):
    # return HttpResponseGone ("gu")
    return render(reuest,'shop/hello.html')