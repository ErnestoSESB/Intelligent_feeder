from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Tipos de Usuário', {'fields': ('tipos_usuario',)}),
    )

class UsuarioInLine(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'Dados do Usuário'
    fk_name = 'agricultor'

@admin.register(Agricultor)
class AgicultorAdmin(admin.ModelAdmin):
    list_display = ('usuario','cidade','telefone','data_registro')
    inlines = [] 
# Register your models here.