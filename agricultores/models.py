from django.db import models

class Agricultor(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_de_registro = models.DateTimeField(auto_now_add=True)
    
# Create your models here.
