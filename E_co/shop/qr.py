from django.shortcuts import render,redirect
from django.http import HttpResponseGone
from .forms import MyForm
from qrcode import*
from .models import qrname
from io import BytesIO
from django.core.files.base import ContentFile



def formcview(request):
    form = MyForm()
    return render(request , 'shop/show_qr_form.html', {'form': form})


def test(request):
    all_info=qrname.objects.all()
    length=len(all_info)
    return render(request, 'shop/data_view.html',{'all_informations':all_info,'length':length})
def formqr(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            second_name = form.cleaned_data['second_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            image=make(message)

            image_io = BytesIO()
            image.save(image_io, format='JPEG')

            qr_instance = qrname(
                name=name,
                second_name=second_name,
                email=email,
                phone=phone,
                image_information=message,
            )
            qr_instance.image.save('shop/qrimgs/Qrimg.jpg', content=ContentFile(image_io.getvalue()))
            # Save the data to the database
            qr_instance.save()
            return redirect('test')
    else:
        form = MyForm()

    return render(request, 'shop/qr.html', {'form': form})