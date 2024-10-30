# Modulo 2 - Clase 5: Manejo de Excepciones y Debugging

## Ejercicios

### Bloque A - Ejercicio 1

# Entendiendo las excepciones
# * Investigue posibles excepciones aplicables a las listas y diccionarios.
# * Escriba un código que obligue la emergencia de una excepción y captúrela con los bloques try/except. Imprima por pantalla el nombre de la excepción y el mensaje.
# * Tip: para identificar las excepciones que aplican a determinados tipos de datos usted siempre debe recurrir a la documentación oficial.

##Listas
# #IndexError: Ocurre cuando intentas acceder a un índice que está fuera del rango de la lista.
# mi_lista = ["Python","C","C++","JavaScript"]
# buscar_ind = 5
# try:
#     print(mi_lista[buscar_ind])
# except IndexError:
#     print("Lo siento, el indice esta fuera de rango")

# #ValueError - Al usar métodos como .index() con un valor que no existe:
# lista = [1, 2, 3]
# try:
#     posicion = lista.index(10)  # Provocará ValueError
# except ValueError:
#     print("El elemento no está en la lista")

# #TypeError: Sucede si intentas realizar operaciones con tipos incompatibles en listas, como concatenar una lista con un número o intentar usar un índice que no sea un número entero.
# try:
#     print(lista["a"])  # Los índices deben ser enteros, no cadenas
# except TypeError:
#     print("¡Error! El índice debe ser un número entero.")

    
# ##Diccionarios

# #KeyError - Al intentar acceder a una clave que no existe:
# diccionario = {"a": 1, "b": 2}
# try:
#     valor = diccionario["c"]  # Provocará KeyError
# except KeyError:
#     print("La clave no existe en el diccionario")

# ##TypeError - Al usar un tipo de dato inmutable como clave:
# try:
#     diccionario = {[1,2]: "valor"}  # Provocará TypeError
# except TypeError:
#     print("No se pueden usar listas como claves")


# ##En listas y diccionario
# #AtributeError: Ocurre cuando intentas acceder a un atributo o método que no existe para el tipo de objeto.
# lista = [1, 2, 3]
# try:
#     lista.appendd(4)  # 'appendd' no es un método válido
# except AttributeError:
#     print("¡Error! Método incorrecto para listas.")


### Bloque A - Ejercicio 2
# Mejorando el código con manejo de excepciones
# * Utilice el código creado en la clase anterior (el problema de la distancia geodésica) y mejórelo con manejo de excepciones.
# * Investigue los valores posibles de las latitudes y longitudes.
# * Incorpore excepciones de tipo ValueError a ser lanzadas cuando se intente crear un objeto con valores de latitude y/o longitude erróneas.
# * Pruebe su código forzando la aparición de estas excepciones y capturándolas para mostrar el resultado erróneo.

#Posibles excepciones: Rangos de lat, lng, y altitu

# import geopy.distance



# class Position:
#     def __init__(self, latitud, longitud, altitud):
        
#         if not isintance(latitud, (float)):
#         self.latitud = latitud
#             raise TypeError(f"Latitud debe ser float")
# # if type(latitud) is not float or type(longitud) is not float or type(altitud) is not float:
# #    raise ValueError("El valor ingresado no es correcto")
#         if not self.validar_latitud(latitud):
#             raise ValueError("Latitud no valida")

#         self.longitud = longitud
#         self.altitud = altitud

#     def __str__(self):
#         return f"latitud: {self.latitud}, longitud: {self.longitud}, altitud: {self.altitud}"

#     def validar_latitud(latitud):
#         return -90 <= latitud <= 90

# class Distance:
#     def __init__(self, source, destination):
#         self.source = source
#         self.destination = destination

#     def km(self):        
#         return geopy.distance.geodesic(
#             (self.source.latitud, self.source.longitud),
#             (self.destination.latitud, self.destination.longitud)
#         ).km
    

# # Valparaiso
# try:
#     pos1 = Position(-33.047237, -71.612686, 10)
# except(ValueError, TypeError) as e :
#     print(e)
# # Santiago
# pos2 = Position(-33.447487, -70.673676, 520)


# distance = Distance(pos1, pos2)
# print(f"La distancia geodésica es de {distance.km():.2f} km.")



### Bloque B - Ejercicio 1
# Base de ejercicio
# * Incorpore el siguiente código en su IDE y estúdielo.
#   ```python

# FIN = False
# registro_llamado = {"frecuencia": None, "motivo": None, "fecha": None}
# listado_llamados = []
# while not FIN:
#     frecuencia = input("Ingrese frecuencia: ")
#     if frecuencia == "FIN":
#         FIN = True
#     else:
#         motivo = input("Ingrese motivo: ")
#         fecha = input("Ingrese fecha: ")
#         registro_llamado["frecuencia"] = frecuencia
#         registro_llamado["motivo"] = motivo
#         registro_llamado["fecha"] = fecha
#         listado_llamados.append(registro_llamado)
# print(listado_llamados)


### Bloque B - Ejercicio 2

# Debugging de código
# * Una vez que haya estudiado y ejecutado el código, identifique el principal resultado erróneo.
# * Identifique líneas que sean de su interés, actívelas como puntos de suspensión (breakpoint) y ejecute un proceso de debugging.
# * Discuta el problema subyacente y corrija el código para que este funcione adecuadamente.
    


FIN = False

registro_llamado = {"frecuencia": None, "motivo": None, "fecha": None}
listado_llamados = []

while not FIN:
    frecuencia = input("Ingrese frecuencia: ")

    if frecuencia == "FIN":
        FIN = True
    else:
        motivo = input("Ingrese motivo: ")
        fecha = input("Ingrese fecha: ")

        registro = {}
        
        registro["frecuencia"] = frecuencia
        registro["motivo"] = motivo
        registro["fecha"] = fecha

        listado_llamados.append(registro_llamado)
        
print(listado_llamados)
