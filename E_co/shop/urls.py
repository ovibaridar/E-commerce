from django.urls import path ,include
from .import views
from .import about


urlpatterns = [

    path('', views.shophome, name='shophome'),
    path('about', about.about, name='about'),
    path('qrcode',views.qrcode, name='qrcode'),
    path('genarator',views.genarator, name='genarator'),

    # path('E_co/', include('E_co.urls'))

]