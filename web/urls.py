  
"""
URL configuration for PersonalPage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path 
from . import views


urlpatterns = [
     path("" ,  views.web , name = "web"),
     path('landings/' , views.landings , name = 'landings'),
     path('portfolios/' , views.portfolios , name = 'portfolios'),
     path('corporativas/' , views.corporativas , name = 'corporativas'),
     path('tiendas/' , views.tiendas , name = 'tiendas'),
     path('blogs/' , views.blogs , name = 'blogs'),
     path('educativas/' , views.educativas , name = 'educativas'),
     #path('personalizadas/' , views.personalizadas , name = 'personalizadas'),
]
 

    