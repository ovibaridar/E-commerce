from django.urls import path ,include
from .import views
from .import about
from .import qr



urlpatterns = [

    path('', views.shophome, name='shophome'),
    path('about', about.about, name='about'),
    path('qrcode',views.qrcode, name='qrcode'),
    path('genarator',views.genarator, name='genarator'),
    path('formcview',qr.formcview, name='formcview'),
    path('test',qr.test, name='test'),
    path('formqr',qr.formqr, name='formqr')

    # path('E_co/', include('E_co.urls'))

]