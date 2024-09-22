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


