# Concatenación de strings
palabra_uno = "Hola"
palabra_dos = "Mundo"
print(palabra_uno + " " + palabra_dos)

# Slice ("rebanada") es con i<=x<j (i incluido, j excluido) entonces siempre se tiene que tomar un valor más
nombre = "Juan nieve"
print(nombre[0:7])

# slice inverso (de derecha a izquierda)
nombre = "Juan nieve"
print(nombre[::-1])


# slice inverso (de derecha a izquierda) [0:3] 0 incluido, 3 excluido. 
nombre = "Juan nieve"
print(nombre[::-1][0:3])

'''
se usan después de una definición de una función
Puede que se ocupen para docstring, ayuda a generar el código
'''

# Se usa con la coma para concatenar
edad = int(input("Ingresa tu edad: "))
print("Tu edad es: ", edad)

# Se usa con el signo + para concatenar, pero tiene que ser con un string.
edad = int(input("Ingresa tu edad: "))
print("Tu edad es: " + str(edad))



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


a = 5
b = 10

if a > b:
    print("a es mayor que b")


i = 1 
while i < 6:
    print(i)
    i += 1

for i in range(1, 6):
    print(i)

# considerar que existe el break y el continue. El break rompe el ciclo y el continue lo salta.

# funciones
def mi_funcion():
    print("Hola desde mi función")

mi_funcion()