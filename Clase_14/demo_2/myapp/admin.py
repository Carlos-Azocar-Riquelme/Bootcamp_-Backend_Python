from django.contrib import admin
from .models import Producto, Etiqueta, Categoria
# Register your models here.

admin.site.register(Producto)
admin.site.register(Etiqueta)
admin.site.register(Categoria)


