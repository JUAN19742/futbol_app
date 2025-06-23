from django.shortcuts import render


def index(request):
    return render(request, 'futbol/index.html')

def equipos(request):
    return render(request, 'futbol/equipos.html')

def contacto(request):
    return render(request, 'futbol/contacto.html')

