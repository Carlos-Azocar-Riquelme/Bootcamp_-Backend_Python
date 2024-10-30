
# Crear una lista con los siguientes números:10, 20, 5, 60, 20, 10(en este orden).
# Determine el rango del conjunto de números 
# Determine el promedio haciendo uso del ciclo for
# Determine el promedio haciendo uso de las funciones genéricas queaplican sobre la lista.

# lista = [10, 20, 5, 60, 20, 10]
# min = min(lista)
# max = max(lista)
# rango = max - min

# print(f"El menor número es: {min}")
# print(f"El máx número es: {max}")
# print(f"El rango es: {rango}")


# Desarrolle un programa que permita almacenar y calcular el promedio de nota sde cinco estudiantes en una escuela. 
# Cada estudiante tiene tres calificacionesen un rango de 1 a 7.
# El sistema debe solicitar los datos de los estudiantes y susnotas al usuario y luego mostrar el promedio de calificaciones de cadaestudiante.

    # Crear un programa que solicite el nombre de cada uno de los cincoestudiantes. Para cada estudiante, solicite tres notas.
    # b. Almacenar los datos de cada estudiante (nombre y lista de notas) en unalista de listas.
    # c. Calcular el promedio de notas para cada estudiante. Mostrar el nombre de cada estudiante junto con su promedio.


from typing import Final


contador_estudiante = 0
lista_estudiantes = []

for contador_estudiante in range(1,2):

    nombre_estudiante = input(f"Ingrese el nombre del/la estudiante {contador_estudiante}: ")
    notas = []
    nota = 0
    while nota < 4:
        nota_estudiante= float(input(f"Ingrese la nota {nota}:"))
        if nota_estudiante >= 1  and nota_estudiante  <= 7:
            notas.append(nota_estudiante)
            nota +=1
        else:
            print("Ingrese una nota válida entre 1 y 7")

    lista_estudiantes.append([nombre_estudiante, notas])

print(lista_estudiantes)


# Desarrolla un programa que permita registrar el nombre y apellido de varias personas,almacenando cada registro en un diccionario y organizando todos los registros en unalista.a. Solicita al usuario los datos de cada persona. Cada persona debe seralmacenada en un diccionario con las claves "nombre" y "apellido".b. Guarda cada diccionario en una lista llamada personas. Cada vez que seingresen los datos de una persona, crea un diccionario y agrégalo a la listapersonas.c. El programa debe continuar solicitando datos hasta que el usuario ingrese "FIN"como nombre.d. Mostrar la lista de personas. Recorre la lista personas e imprime el nombre yapellido de cada persona registrada.

Final = False
personas = []
while not Final:
    nombre = input("Ingrese el nombre de la persona: ")
    apellido = input("Ingrese el apellido de la persona: ")
    if nombre == "FIN":
        Final = True
    else:
        persona = {
            "nombre": nombre,
            "apellido": apellido
        }
        personas.append(persona)

for persona in personas:
    print(f"Nombre: {persona['nombre']}, Apellido: {persona['apellido']}")


# Incrementar la funcionalidad del programa anterior permitiendo que ahora cadapersona cuente con cursos inscritos.• Es decir, necesitamos que cada persona contenga un diccionario con clavescorrespondientes a cursos y cada clave con una lista con las notas de dicho curso.• Todos los datos deben ser solicitados por la entrada estándar. Puede consideraringresar un curso por persona. Cada curso tendrá 3 notas.• Al finalizar, el programa debe imprimir el nombre y apellido, seguido del listado decursos y los promedios obtenidos en cada curso.

Final = False
personas = []
while not Final:
    nombre = input("Ingrese el nombre de la persona: ")
    apellido = input("Ingrese el apellido de la persona: ")
    if nombre == "FIN":
        Final = True
    else:
        persona = {
            "nombre": nombre,
            "apellido": apellido,
            "cursos": []
        }
        curso = input("Ingrese el nombre del curso: ")
        notas = []
        for i in range(3):
            nota = float(input(f"Ingrese la nota {i + 1} del curso: "))
            notas.append(nota)
        persona["cursos"].append({curso: notas})
        personas.append(persona)