# urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.sketch, name='sketch'),
    path('sketch_conversion/', views.sketch_conversion, name='sketch_conversion'),
]

# Add the following to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
