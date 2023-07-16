from django.urls import path
from .import views

urlpatterns = [

    path('', views.myprofilehome, name='myprofile')
]