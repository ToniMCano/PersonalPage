from django.shortcuts import render

# Create your views here.


def software(request):
    
    return render(request , "software/desarrollo-de-software.html" , {'title': 'Desarrollo de Software a Medida | Soluciones Personalizadas para tu Empresa'})


def empresarial(request):
    
    return render(request , "software/sistemas-de-gestion-empresarial.html" , {'title': 'Desarrollo de Software a Medida | Soluciones Personalizadas para tu Empresa'})

