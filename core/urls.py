from django.contrib import admin
from django.urls import path , include

from  . import views 
from core import urls
from django.conf import settings


urlpatterns = [
    path("" , views.home , name = "home"),
    path("about/" , views.about , name = "about"),
    path("services/" , views.services , name = "services"),
    path("portfolio/" , views.portfolio , name = "portfolio"),
    path("blog/" , views.blog , name = "blog"),
    path("contacto/" , views.contact , name = "contacto")
]

if settings.DEBUG:
    
    from django.conf.urls.static import static
    
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
