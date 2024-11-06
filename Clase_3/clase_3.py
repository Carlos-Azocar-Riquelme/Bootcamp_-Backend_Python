from functools import reduce


# FUNCIONES ANÓNIMAS

lambda x: x + 1

(lambda x: x + 1)(2)

print((lambda x: x + 1)(2))

# Esto no es recomendado
cuadrado = lambda x: x ** 2
print(cuadrado(2))


lambda x, y: x + y

(lambda x, y: x + y)(2, 3)
print((lambda x, y: x + y)(2, 3))
print((lambda x, y: x + y)('hola', ' Carlos'))
print((lambda x, y: x + y)([1,2],[3, 4]))

valor = (lambda x, y: x + y)(2, 3)

for valor in range(10):
    print((lambda x: x + 1)(valor))

print(f"Este es el valor {valor}")
print(lambda x, y: x + y)


# lambda con decisiones

lambda x, y: "x es mayor" if (x>y) else "x es menor"

print ((lambda x, y: "x es mayor" if (x>y) else "x es menor")(2,3))

print((lambda x : x**2)(2))

cuadrado = lambda x: x**2
print(cuadrado(2))

print((lambda x, y : "x mayor que y" if (x>y) else "x menor que y")(1,2))


lista_nueva = list(map(lambda x: x**2, [1,2,3,4,5]))
print(lista_nueva)


lista_original = [4,4]
raiz_cuadrada = list(map(lambda x: x**0.5, lista_original))
print(raiz_cuadrada)


lista=  [1,2,3,4,5]
lista_nueva = list (filter(lambda x: x>2,lista))

print(lista_nueva)

resultado = reduce(lambda x, y: x + y, lista)

# Map

lista_original = [2,4,5]

lista_cuadrados = list(map(lambda x: x**2, lista_original))

print(lista_original)
print(lista_cuadrados)

# Filter

lista_filtrada = list(filter(lambda x: x>16, lista_cuadrados))
print(lista_filtrada)

# Reduce

multiplicacion = reduce(lambda x, y: x*y, lista_original)
print(multiplicacion)