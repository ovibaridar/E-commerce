from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def shophome(request):
    return render(request, 'shop/shop.html')

def about(request):

    return render(request, 'shop/about.html')

def acount(request):

    return render(request, 'shop/acount.html')

def chakeout(request):

    return render(request, 'shop/chakeout.html')

def productview(request):

    return render(request, 'shop/productview.html')

def search(request):
    return render(request, 'shop/search.html')
