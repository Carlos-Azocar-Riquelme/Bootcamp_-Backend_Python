# from functools import reduce


# lista= [1,2,3,40, 4,5, -1, 0]
# # valor_mayor = reduce((lambda x, y : x if  x > y else y), lista)
# valor_mayor = reduce((lambda x, y : x if  x > y else y), lista)


# print(valor_mayor)


# Cree un programa que solicite el nombre de una estación de monitoreo y los vientos registrados(nudos)
# en las últimas 5, 10, y 15 horas.• Almacene esta información en la memoria principal usando diccionarios y listas.
# • Su programa debe crear un nuevo diccionario con los vientos registrados en kilómetros por hora.
# • Además, el programa debe mostrar por la salida estándar el nombre de la estación y los vientos registrados
# (convertidos a kilómetros por hora).• Debe usar operación map()

nombre_estacion = input("Ingrese el nombre de la estación: ")
lista_registros = []


vientos_registros = { 
                        "5 horas": 0,
                        "10 horas": 0, 
                        "15 horas":0
                    }

for tiempo in vientos_registros:
    registro= input(f"Ingrese el registro en nudos a las {tiempo}: ")
    vientos_registros[tiempo] = int(registro)
    
lista_registros = list(map((lambda x : x * 1.852), vientos_registros.values()))
print(lista_registros)

i=0
for tiempo in vientos_registros:
    vientos_registros[tiempo] = float(lista_registros[i])
    i += 1

registro= {
    "nombre_estacion": nombre_estacion,
    "vientos_registros": vientos_registros
}
print(registro)


# 1 nudo = 1.852 kilómetros por hora

