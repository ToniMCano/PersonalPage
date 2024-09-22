from django.shortcuts import render

# Create your views here.



def ia(request):
    
    return render(request , "ia/ia.html" , {'title':'Soluciones basadas en Inteligencia Artificial'})


def analisis(request):
    
    return render(request , "ia/analisis-predictivo.html" , {'title': 'Análisis Predictivo: Descubre el Futuro de tus Datos'})


def automation(request):
    
    return render(request , "ia/automatizacion-inteligente.html" , {'title': 'Automatización Inteligente: La Clave para Transformar Tu Negocio'})


def chat(request):
    
    return render(request , "ia/chatbots-y-asistentes-virtuales.html" , {'title' : 'Chatbots y Asistentes Virtuales: Transforma tu Negocio con IA'})
