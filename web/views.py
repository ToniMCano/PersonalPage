from django.shortcuts import render

# Create your views here.


def web(request):
    
    return render(request , "web/desarrollo-web-profesional.html" , {'title' : 'Desarrollo Web Profesional a Medida | Sitios Web Personalizados'})
