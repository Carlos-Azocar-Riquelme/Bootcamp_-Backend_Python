# Ejercicio 1: Cálculo de la Raíz Cuadrada

numero = int(input("Ingresa un número: "))
raiz_cuadrada = numero ** 0.5
print("La raíz cuadrada de ", numero, " es: ", raiz_cuadrada)

# Ejercicio 2: Distancia euclidiana entre dos puntos

x1 = int(input("Ingresa el valor de x1 para el punto 1: "))
y1 = int(input("Ingresa el valor de y1 para el punto 1: "))
x2 = int(input("Ingresa el valor de x2 para el punto 2: "))
y2 = int(input("Ingresa el valor de y2 para el punto 2: "))
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("La distancia euclidiana entre los puntos (", x1, ",", y1, ") y (", x2, ",", y2, ") es: ", distancia)

# Ejercicio 3: Invertir palabras

palabra = input("Ingresa una palabra: ")
palabra_invertida = palabra[::-1]
print("La palabra original es: ", palabra)
print("La palabra invertida es: ", palabra_invertida)