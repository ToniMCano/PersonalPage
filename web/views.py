from django.shortcuts import render

# Create your views here.


def web(request):
    
    return render(request , "web/desarrollo-web-profesional.html" , {'title' : 'Desarrollo Web Profesional a Medida | Sitios Web Personalizados'})


def landings(request):
    
    return render(request , 'web/landing-pages.html' , {'title' : 'Landing Pages'})


def tiendas(request):
    
    return render(request , 'web/tiendas-online.html' , {'title' : 'Tiendas Online'})


def portfolios(request):
    
    return render(request , 'web/portfolios-y-sitios.profesionales.html' , {'title' : 'Portfolio y Sitios Web Personales'})


def blogs(request):
    
    return render(request , 'web/blogs-y-portales-de-contenido.html' , {'title' : 'Blogs y Portales de Contenido'})


def educativas(request):
    
    return render(request , 'web/plataformas-educativas.html' , {'title' : 'Plataformas Educativas'})


'''def personalizadas(request):
    
    return render(request , 'web/aplicaciones-web-personalizadas.html' , {'title' : 'Aplicaciones Web Personalizadas'})
'''

def corporativas(request):
    
    return render(request , 'web/sitios-web-corporativos.html' , {'title' : 'Páginas Web Corporativas'})