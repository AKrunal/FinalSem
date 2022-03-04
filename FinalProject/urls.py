from django.contrib import admin
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('signin_up/',include('login.urls')),
    path('api/',include('api.urls')),
    path('order/',include('order.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
