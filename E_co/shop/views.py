from django.shortcuts import render
from django.http import HttpResponseGone
from .models import product
from qrcode import*
# import qrcode
# Create your views here.
def shophome(request):

    all_products = product.objects.all()


    # return HttpResponseGone ("gu")
    return render(request,'shop/hello.html', {'products': all_products })


def genarator(request):

    return render(request,'shop/Qrcode.html')




def qrcode(request):
    value = 0
    data = request.POST.get('data', '')

    if data == "":
        error = "Enter your text here"
        proms = {'error': error}
        return render(request, 'shop/Qrcode.html', proms)
    img = make(data)
    img.save('shop/static/qrimg/Qrimg.jpg')
    proms = { 'img': img}
    return render(request, 'shop/Qrcode.html', proms)





