from django.urls import path
from .import views

urlpatterns = [

    path('', views.shophome, name='shop'),
    path('productview', views.productview, name='view'),
    path('acount', views.acount, name='acount'),
    path('search', views.search, name='search'),
    path('about', views.about, name='about'),
    path('chakeout', views.chakeout, name='chakeout'),
]
