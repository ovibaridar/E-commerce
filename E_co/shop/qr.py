from django.shortcuts import render

def formqr(request):
    return render(request , 'shop/qr.html')