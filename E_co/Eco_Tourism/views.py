from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def EcoHome(request):
    return render(request,'Eco_Tourism/Home page.html')
