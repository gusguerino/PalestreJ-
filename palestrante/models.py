from django.db import models
from django.conf import settings


class Palestra(models.Model):
    palestrante = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class Pergunta(models.Model):
    palestra = models.ForeignKey(
        'Palestra', on_delete=models.CASCADE)
    pergunta = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    feita_em = models.DateTimeField(auto_now_add=True)
    aceita_em = models.DateTimeField(null=True)

    def __str__(self):
        return "{}: {}".format(self.autor, self.pergunta)
