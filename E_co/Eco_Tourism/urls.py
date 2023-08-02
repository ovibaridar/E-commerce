from django.urls import path
from .import views

urlpatterns = [

    path('', views.EcoHome, name='home'),
    path('eco_tours', views.eco_tours, name='eco_tours'),
    path('eco_hotels', views.eco_hotels, name='eco_hotels'),
    path('Travel_Tips', views.Travel_Tips, name='Travel_Tips'),
    path('Photo_and_Videos', views.Photo_and_Videos, name='Photo_and_Videos'),
    path('Sustainability', views.Sustainability, name='Sustainability'),
    path('Booking', views.Booking, name='Booking'),
    path('Testimonials', views.Testimonials, name='Testimonials'),
    path('About_Us', views.About_Us, name='About_Us'),
    path('Contact', views.Contact, name='Contact'),
    path('blog', views.blog, name='blog')
]