# # modularizar los ejercicios anteriores

# # Ejercicio 1: Cálculo de la Raíz Cuadrada

# numero = int(input("Ingresa un número: "))
# raiz_cuadrada = numero ** 0.5
# print("La raíz cuadrada de ", numero, " es: ", raiz_cuadrada)

# # Ejercicio 2: Distancia euclidiana entre dos puntos

# x1 = int(input("Ingresa el valor de x1 para el punto 1: "))
# y1 = int(input("Ingresa el valor de y1 para el punto 1: "))
# x2 = int(input("Ingresa el valor de x2 para el punto 2: "))
# y2 = int(input("Ingresa el valor de y2 para el punto 2: "))
# distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# print("La distancia euclidiana entre los puntos (", x1, ",", y1, ") y (", x2, ",", y2, ") es: ", distancia)


# # Ejercicio 3: Invertir palabras

# palabra = input("Ingresa una palabra: ")
# palabra_invertida = palabra[::-1]
# print("La palabra original es: ", palabra)
# print("La palabra invertida es: ", palabra_invertida)

# # determinar si una palabra es un palíndromo

# palabra = input("Ingresa una palabra: ")
# palabra_invertida = palabra[::-1]
# if palabra == palabra_invertida:
#     print("La palabra es un palíndromo")
# else:
#     print("La palabra no es un palíndromo")


# # Determinar si un número se encuentra en un rango determinado

# numero = int(input("Ingresa un número: "))





# Trabajo grupal – Ejercicio #4• Escriba un programa que continuamente pregunte por un número hasta que seescriba la palabra “FIN”.
#  En cada ciclo el programa debe actualizar el valor mayor y reportarlo por pantalla.• 
# Si no ingresa un valor mayor al anterior, el programa debe continuar mostrando elúltimo valor considerado como mayor.• 
# ¿Podría reescribir el programa para determinar el número menor?• Nota: no se puede usar instrucción de tipo break.

numero = 0
mayor = 0
while numero != "FIN":
    numero = input("Ingresa un número: ")
    if numero == "FIN":
        break
    numero = int(numero)
    if numero > mayor:
        mayor = numero
    print("El número mayor es: ", mayor)


