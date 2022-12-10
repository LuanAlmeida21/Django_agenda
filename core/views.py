from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
# Create your views here.

def titulo_evento(request, titulo_evento):
    local = Evento.objects.get(titulo= titulo_evento)
    return HttpResponse(f'<h1>{local}</h1>')

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

#def index(request):
#    return redirect('/agenda/')


# eventos.objects.all() - pega todos objetos
# filter(usuario=usuario) - usuario logado

