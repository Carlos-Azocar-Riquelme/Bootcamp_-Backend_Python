
# class Persona:
#     nombre= "Juan Pérez"

#     def get_nombre(self):
#         return self.nombre

# x  = Persona()
# print(x.get_nombre())

# y = Persona()
# print(x.get_nombre())

# print(id(x))
# print(id(y))


# self es para indicar al objeto en si mismo y ejecutate sobre ese objeto.
# también indicar cuando son variables que le partenecen a la clase

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.apellido = None

    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
x  = Persona("Carlos")
y = Persona("Camilo")
print(x.get_nombre())
print(x.get_apellido())
print(y.get_nombre())

print(id(x))
print(id(y))

# abstracción más específica se llama subclass su es generar en super Class

