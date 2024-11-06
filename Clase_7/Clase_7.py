import pandas as pd

# # con loc podemos traer una fila

# df = pd.read_csv('titanic.csv')   # cargamos el dataset

# # podemos ver las primeras filas con head
# print(f'El head es {df.head()}')

# # podemos ver las ultimas filas con tail
# print(f'El tail es {df.tail()}')

# # podemos ver la cantidad de filas y columnas con shape
# print(df.shape)

# # podemos ver los nombres de las columnas con columns
# print(df.columns)

# # podemos ver los tipos de datos de las columnas con dtypes
# print(df.dtypes)

# # podemos ver un resumen de los datos con info
# print(df.info())

# # podemos ver un resumen estadistico
# print(df.describe())


# # Crear un DataFrame a partir de un diccionario
# data = {
#     'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
#     'Edad': [23, 34, 45, 22],
#     'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
# }


# df = pd.DataFrame(data)
# print('')
# print('')
# print('DataFrame')
# print(df)
# print('')
# print('')

# print('primera fila')
# print(df.loc[0])  # traemos la primera fila
# print('')
# print('')

# print('primera columna')
# print(df.head(2))  # traemos las dos primeras filas
# print('')
# print('')

# print('ultima fila')
# print(df.tail(2))  # traemos las dos ultimas filas
# print('')
# print('')

# print('Resumen estadístico')
# print(df.describe())  # resumen estadistico
# print('')
# print('')

# print('Resumen de datos')
# print(df.info())  # resumen de los datos



# Crear un DataFrame a partir de un diccionario
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad': [23, 34, 45, 22],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla'],
    'Peso': [55, 78, 85, 60],  # Peso en kilogramos
    'Altura': [1.65, 1.80, 1.75, 1.60]  # Altura en metros
}

df = pd.DataFrame(data)

# Definir una función para calcular el IMC
def calcular_imc(row):
    return row['Peso'] / (row['Altura'] ** 2)

df['IMC'] = df.apply(calcular_imc, axis=1)

print('DataFrame con IMC')
print(df)