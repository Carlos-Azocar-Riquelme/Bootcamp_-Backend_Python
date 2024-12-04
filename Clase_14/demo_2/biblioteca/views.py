from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Libro

# Create your views here.
class LibroListView(View):
    def get(self, request):
        #libros = Libro.objects.values('titulo', 'genero__nombre','autor')
        libros = Libro.objects.all()
        data = []

        for libro in libros:
            libro_data = {
                "nombre": libro.titulo,
                "autores": [autor.nombre for autor in libro.autores.all()]
            }
            data.append(libro_data)

        print('libros', libros)
        response = {
            "total": len(data),
            "libros": data
        }
        print(response)
        return JsonResponse(response)