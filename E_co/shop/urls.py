from django.urls import path ,include
from .import views

urlpatterns = [

    path('', views.shophome, name='shophome'),
    # path('E_co/', include('E_co.urls'))

]