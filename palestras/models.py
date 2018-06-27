from django.db import models
from django.conf import settings


class Palestra(models.Model):
    palestrante = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200, verbose_name="Descrição")

    def __str__(self):
        return self.titulo
    
    def quantidade_perguntas(self):
        return self.perguntas.count()
        
    def quantidade_perguntas_aceitas(self):
        return self.perguntas.filter(aceita_em__isnull = False).count()

class Pergunta(models.Model):
    palestra = models.ForeignKey(
        'Palestra', related_name='perguntas', on_delete=models.CASCADE)
    pergunta = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    feita_em = models.DateTimeField(auto_now_add=True)
    aceita_em = models.DateTimeField(blank=True, null=True)

    def foi_aceita(self):
        return True if self.aceita_em else False
        
    def __str__(self):
        return "{}: {}".format(self.autor, self.pergunta)
