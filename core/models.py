from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#blank = the field can be empty
#auto_now = add date current into field
#CASCADE = se o usuario for deletado, exclui todos os eventos dele


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 

    class Meta:
        db_table = 'evento'

    #retorna o nome do evento igual ao titulo
    def __str__(self):
        return self.titulo
        