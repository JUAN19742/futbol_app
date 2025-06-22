from django.shortcuts import render
from .models import Equipo

def index(request):
    return render(request , 'futbol/index.html')
                   
def equipos(request):
    lista = Equipo.objects.all()
    return render(request, 'futbol/equipos.html' , {'equipos':lista})
                                                    
def contacto(request):
    if request.method == 'POST':
        return render(request , 'futbol/contacto.html' , { 'mensaje': 'Gracias ␣ por ␣ contactarnos!'})
    return render( request , 'futbol/contacto.html')

