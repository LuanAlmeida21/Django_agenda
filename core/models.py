from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.

#blank = the field can be empty
#auto_now = add date current into field
#CASCADE = se o usuario for deletado, exclui todos os eventos dele

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    local = models.CharField(blank=True, null=True, max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 

    class Meta:
        db_table = 'evento'

    #retorna o nome do evento igual ao titulo
    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')

    def get_data_evento_input(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False
    
    def get_evento_hora(self):
        data_atrasado = datetime.now() + timedelta(hours=1)
        if (datetime.now() < self.data_evento) and (self.data_evento < data_atrasado):
            return True
        else:
            return False
        

        