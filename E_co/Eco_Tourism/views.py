from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def EcoHome(request):
    par={'active':"active"}
    return render(request,'Eco_Tourism/Home page.html',par)