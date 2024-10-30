# EJERCICIO 1

# Cree las clases Waypoint y Trackpoint.
# La clase Waypoint contiene un nombre; la clase Trackpoint contiene una fecha de registro.
# Ambas clases son posiciones geográficas de tipo Position.
# La clase Position requiere en su inicialización una latitud, una ongitud y una altitud


# import geopy.distance import geodesic

class Position:
    def __init__(self, latitud, longitud, altitud):
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud

    def to_string(self):
        return f"Latitud: {self.latitud} , Longitud: {self.longitud} , Altitud: {self.altitud}"

    def to_dict(self):
        return {
            "latitud": self.latitud,
            "longitud": self.longitud,
            "altitud": self.altitud
        }


class Waypoint(Position):
    def __init__(self, nombre,latitud,longitud,altitud):
        super().__init__(latitud,longitud,altitud)
        self.nombre = nombre

    def to_string(self):
        return f"Nombre: {self.nombre} , {super().to_string()}"
    
    def to_dict(self):
        data = super().to_dict()
        data["nombre"] = self.nombre
        return data
    
    #Ejemplo str
    #def __str__(self):
    #    return f"Waypoint(name: {self.name},{super().__str__()})"

class Trackpoint(Position):
    def __init__(self, fecha_registro,latitud, longitud, altitud):
        super().__init__(latitud, longitud, altitud)
        self.fecha_registro = fecha_registro
    
    def to_string(self):
        return f"Fecha Registro: {self.fecha_registro} , {super().to_string()}"
        
    def to_dict(self):
        data = super().to_dict()
        data["fecha_registro"] = self.fecha_registro
        return data
    
    # def to_dict(self)
    #     #diccionario = dict("Fecha Registro: {self.fecha_registro} , {super().to_string()}")


waypoint_one = Waypoint("Place one", 1232131, 234234234, 23432423)
trackpoint_one = Trackpoint("22/10/2024", 234234, 12334454, 12312312 )


#Retorno de Waypoint
print(waypoint_one.to_string())
print(trackpoint_one.to_string())

print(waypoint_one.to_dict())
print(trackpoint_one.to_dict())




# print(waypoint_one.nombre)
# print(waypoint_one.latitud, waypoint_one.longitud, waypoint_one.altitud)



# EJERCICIO 2

# Múltiples representaciones
# Cree dos representaciones para los objetos de tipo posición:
# Una representación de atributos separados por coma (string)
# Una representación de atributos como diccionario.


# EJERCICIO 3

# pip Install geopy

# Distancia geodésica
# Importe la biblioteca “geopy” para hacer uso de la función de istancia geodésica (import geopy.distance).

# Cree una clase “helper” llamada Distance que se inicialice con dos osiciones: una posición de origen y una posición de destino.

# Cree un método llamado “km(self)” que retorne la distancia geodésica en kilómetros.

# return geopy.distance.geodesic(
#             ((self.source.__dict__())["latitude"],
#              (self.source.__dict__()["longitude"])),
#             ((self.destination.__dict__())["latitude"],
#              (self.destination.__dict__()["longitude"]))
#         ).km


# EJERCICIO COMPARTIDO POR EL PROFESOR

# import geopy.distance

# class Position:
#     def __init__(self, latitude, longitude, altitude):
#         self.latitude = latitude
#         self.longitude = longitude
#         self.altitude = altitude

#     def __dict__(self):
#         return {"latitude": self.latitude, "longitude": self.longitude, "altitude": self.altitude}

# class Waypoint(Position):
#     def __init__(self, nombre, latitude, longitude, altitude):
#         self.nombre = nombre
#         super().__init__(latitude, longitude, altitude)

# class Trackpoint(Position):
#     def __init__(self, fecha, latitude, longitude, altitude):
#         self.nombre = fecha
#         super().__init__(latitude, longitude, altitude)

# ciudad1 = Waypoint("Centro", -33, -70, 650)
# ciudad2 = Waypoint("CentroSur", -38, -70, 650)

# print(ciudad1.__dict__())
# print(ciudad2.__dict__())

# # (elemento, elemento2, elemento3, ....)
# # pos1 = (lat, long)
# # pos2 = (lat, long)

# print(geopy.distance.geodesic(
#     (ciudad1.__dict__()["latitude"], ciudad1.__dict__()["longitude"]),
#     (ciudad2.__dict__()["latitude"], ciudad2.__dict__()["longitude"]),
#     ).km
# )