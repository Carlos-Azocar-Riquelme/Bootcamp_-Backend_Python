# # listas
# lista = []

# print(lista)
# print(type(lista))


# productos = ['manzana', 'pera', 'naranja', 'banana', 'uva']

# # Agrega al final de la lista un elemento
# productos.append('kiwi')
# print(productos)

# # agrega un elemento a la lista en la posición 2
# productos.insert(2, 'sandia')

# # Elimina el último elemento de la lista
# productos.remove('banana')
# print(f"Los productos que quedan son: {productos}")


# # ordena la lista de forma ascendente
# productos.sort()
# print(f"Los productos ordenados alfabéticamente son: {productos}")

# # ordena la lista de forma descendente  
# productos.sort(reverse=True)

# # invertir el orden de la lista
# productos.reverse()


# # eliminar un elemento de la lista por su posición
# productos.pop(2)
# print(f"Los productos que quedan son: {productos}")
# print(f"El producto eliminado fue: {productos.pop(2)}")


# # ordenar e invertir
# productos.sort()
# productos.reverse()

# for producto in productos:
#     print(f"los productos son {producto}")

# minimo = min(productos)
# maximo = max(productos)
# len(productos)

# print(f"El mínimo es {minimo}, el máximo es {maximo} y la cantidad de productos es {len(productos)}")

# # también está sum, que suma los elementos de la lista
# print(sum([1, 2, 3, 4, 5]))


# # Ejemplo:
# # Gestión de Inventario de ProductosConsidera un sistema de inventario simple para una tienda. 
# # Los productosestán organizados en una lista, y el sistema debe ser capaz de realizar varias
# # operaciones para gestionar el inventario.1. Cree una lista inicial de productos fija.2. 
# # Solicita al usuario que agregue tres nuevos productos.3. Elimina un producto específico.4. 
# # Ordena la lista en orden alfabético.5. Muestra el primer y último producto en orden alfabético

# productos = ['manzana', 'pera', 'naranja', 'banana', 'uva']
# i = 0

# while i < 3:
#     producto_nuevo = input("Ingrese un nuevo producto:")
#     productos.append(producto_nuevo)
#     i += 1

# print(f"los productos son : {productos}")

# productos.remove('pera')
# print(f"los productos después de la eliminación son : {productos}")

# productos.sort()
# print(f"los productos ordenados alfabéticamente son : {productos}")

# print(productos[0], " ", productos[-1])
# print(productos[0], " ", productos[len(productos)-1])


# # DICCIONARIOS

# diccionario = {
#     'cursos': {
#         'taller': 'Python Avanzado',
#         'curso1': 'Introducción a Python',
#         'curso2': 'Python Intermedio'
#     }
# }

# print(diccionario['cursos']['taller'])

# diccionario = {
#     'cursos': {
#         'taller': 'Python Avanzado',
#         'curso1': 'Introducción a Python',
#         'curso2': 'Python Intermedio',
#         'curso3': 'Desarrollo Web con Django',
#         'curso4': 'Análisis de Datos con Pandas'
#     },
#     'talleres': {
#         'taller1': 'Machine Learning',
#         'taller2': 'Deep Learning',
#         'taller3': 'Procesamiento de Lenguaje Natural'
#     },
#     'seminarios': {
#         'seminario1': 'Big Data',
#         'seminario2': 'Ciencia de Datos',
#         'seminario3': 'Inteligencia Artificial'
#     }
# }

# print(diccionario['cursos']['curso3']) 
# print(diccionario['talleres']['taller2']) 
# print(diccionario['seminarios']['seminario1'])  

# Ejemplo: 
# Gestión de Inventario de ProductosConsiderando el enunciado anterior, realicemos lo siguiente:

# 1. Cree un diccionario llamado inventario que representará el inventariode la tienda. El inventario deberá contener nombre, cantidad y preciode tres productos.

# 2. Actualizar la cantidad de un producto solicitando los datos al usuario(nombre de producto a actualizar, y cantidad).

# 3. Mostrar el inventario completo recorriendo el diccionario.

inventario = {
    'codigo1030': {
        "Nombre" : "Teléfono", 
        "Cantidad": 5, 
        "Precio": 1000
    },
    'codigo1040': {
        "Nombre" : "Laptop", 
        "Cantidad": 3, 
        "Precio": 1500
    }
}

print(inventario)

nombre = "Teléfono"
Cantidad = 10

for codigo in inventario:
    if inventario[codigo]['Nombre'] == nombre:
        inventario[codigo]["Cantidad"] = Cantidad
        

print('Inventario actualizado')
for codigo in inventario: 
    print(codigo)
    print(inventario[codigo])
    print(inventario[codigo]['Nombre'])
    print(inventario[codigo]['Cantidad'])


