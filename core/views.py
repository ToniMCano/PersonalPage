from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request , "core/index.html" , {'title' : 'Home'})



def about(request):
    
    return render(request , "core/about.html" , {'title' : 'About'})


def services(request):
    
    return render(request , "core/services.html" , {'title' : 'Servicios'})


def portfolio(request):
    
    return render(request , "core/portfolio.html" , {'title' : 'Portfolio'})


def blog(request):
    
    return render(request , "core/blog.html" , {'title' : 'Blog'})   


def contact(request):
    
    return render(request , "core/contacto.html" , {'title' : 'Contacto'})


def analisis(request):
    
    return render(request , "core/analisis-predictivo.html" , {'title': 'Análisis Predictivo: Descubre el Futuro de tus Datos'})


def automation(request):
    
    return render(request , "core/automatizacion-inteligente.html" , {'title': 'Automatización Inteligente: La Clave para Transformar Tu Negocio'})


def software(request):
    
    return render(request , "core/desarrollo-de-software.html" , {'title': 'Desarrollo de Software a Medida | Soluciones Personalizadas para tu Empresa'})



def chat(request):
    
    return render(request , "core/chatbots-y-asistentes-virtuales.html" , {'title' : 'Chatbots y Asistentes Virtuales: Transforma tu Negocio con IA'})
