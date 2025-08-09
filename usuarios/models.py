from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

class Usuario(AbstractUser):
    TIPOS_USUARIO = [
        ('admin', 'Administrador'),
        ('agricultor', 'Agricultor'),
        ('visitante', 'Visitante'),
    ]
    tipos_usuario = models.CharField(max_length=20, choices=TIPOS_USUARIO, default='visitante')

    def is_agricultor(self):
        return self.tipos_usuario == 'agricultor'


class Agricultor(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username