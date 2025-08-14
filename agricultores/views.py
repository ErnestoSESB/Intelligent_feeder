from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Agricultor

def listar_agricultores(request):
    agricultores = Agricultor.objects.all().order_by('-data_de_registro')
    return render(request, 'agricultores/lista.html', {'agricultores': agricultores})