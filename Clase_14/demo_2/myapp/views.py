from django.shortcuts import render
from django.views.generic import ListView , View
from django.http import JsonResponse
from .models import Producto


# Create your views here.

class ProductoView(View):
    def get(self, request):
        productos = Producto.objects.values("id","nombre","precio")
        return JsonResponse(list(productos), safe= False)
    

# class ProductoViewFiltered(View):
#     def get(self, request):
#         productos = Producto.objects.values("id","nombre","precio")
#         return JsonResponse(list(productos), safe= False)


class ProductListView():
    model = Producto
    template_name = 'lista.html'
    context_object_name = 'Productos'