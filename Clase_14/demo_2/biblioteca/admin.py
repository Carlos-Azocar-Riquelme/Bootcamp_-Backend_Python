from django.contrib import admin
from .models import Autor, Libro, Genero

# Register your models here.
@admin.register(Autor)
class AdminAutor(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_nacimiento']
    fields = ['nombre', 'fecha_nacimiento']


@admin.register(Libro)
class AdminLibro(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_publicacion', 'genero', 'autores']

    def autores(self, obj):
        return ", ".join([autor.nombre for autor in obj.autor.all()])
    autores.shortdescription = 'Autores'

@admin.register(Genero)
class AdminGenero(admin.ModelAdmin):
    list_display = ['nombre']
    fields = ['nombre']

