from django.contrib import admin
from .models import Categoria, Videojuego

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'categoria', 'precio', 'disponible')
    list_filter = ('categoria', 'disponible')
    search_fields = ('titulo',)