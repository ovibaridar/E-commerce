from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def EcoHome(request):
    par = {'home_active': "active" ,'range':range(1, 10)}
    return render(request, 'Eco_Tourism/Home page.html', par)


def blog(request):
    par = {'blog_active': "active"}
    return render(request, 'Eco_Tourism/blog.html', par)


def eco_tours(request):
    par = {'eco_tours_active': "active"}
    return render(request, 'Eco_Tourism/eco_tours.html', par)


def eco_hotels(request):
    par = {'hotels_active': "active"}
    return render(request, 'Eco_Tourism/hotels.html', par)



# dropdwons



def Travel_Tips(request):
    return render(request, 'Eco_Tourism/Travel Tips.html')


def Photo_and_Videos(request):
    return render(request, 'Eco_Tourism/Photo and Videos.html')


def Sustainability(request):
    return render(request, 'Eco_Tourism/Sustainability.html')


def Booking(request):
    return render(request, 'Eco_Tourism/Booking.html')


def Testimonials(request):
    return render(request, 'Eco_Tourism/Testimonials.html')


def About_Us(request):
    return render(request, 'Eco_Tourism/About_Us.html')
def Contact(request):
    return render(request, 'Eco_Tourism/Contact.html')
