from django.db import models

# Create your models here.

#blank = the field can be empty
#auto_now = add date current into field


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'evento'

