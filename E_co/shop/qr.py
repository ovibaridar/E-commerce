from django.shortcuts import render
from django.http import HttpResponseGone
from .forms import MyForm

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
            # Do something with the form data (e.g., save to database)

            # Redirect to a success page
            return HttpResponseGone("ok")
    else:
        form = MyForm()

    return render(request, 'shop/qr.html', {'form': form})