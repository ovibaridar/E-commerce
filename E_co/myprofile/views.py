from django.shortcuts import render

# Create your views here.

def myprofilehome (request):
    return render(request,'myprofile/myprofile.html')
