import pandas as pd

# Instale la biblioteca pandas e impórtela en su proyecto Python.
# • Cree un dataframe con un diccionario, tal como se vio en los ejemplos, con las 
# siguientes columnas, y con 5 datos:
# • Nombre
# • Rut
# • Edad
# • Altura
# • Peso
# • Describa y discuta los datos almacenados en el dataframe (almacene los ruts
# como strings)

data ={
    'Nombre': ["Camila", "Carlos", "Cristobal", "Nicolas", "Stefanya"],
    "Rut": ["18888888-8", "18777777-7", "18666666-6", "18555555-5", "18444444-4"],
    "Edad": [18, 25, 70, 40, 50],
    'Altura': [1.70, 1.80, 1.95, 1.60, 1.65],
    'Peso': [70, 55, 80, 65, 78]
}
personas = pd.DataFrame(data)
print(personas.describe())

# Trabajo grupal – Ejercicio #2
# • Cree las siguientes columnas:
# • Rut estandarizado
# • Dígito verificador
# • Índice de masa corporal (IMC)
# • Clasificación de edad (mayor de 30 años, menor de 30 años, mayor de 60 
# años).


# Rut estandarizado
    
personas[["Rut estandarizado", "digito verificador"]] = personas["Rut"].str.split('-',expand=True) #.apply(lambda c: pd.Series(separar_rut(x)))

print(personas)
    
# Índice de masa corporal
def calcular_imc(row):
    return row['Peso'] / (row['Altura'] ** 2)
personas['IMC'] = personas.apply(calcular_imc, axis=1)


# Clasificación de edad
personas['Clasificacion_edad'] = personas.apply(
    lambda x: "mayor de 60" if
    (x["Edad"] > 60) else
    ("mayor de 30" if x["Edad"] > 30 else "menor de 30"), axis=1
)


print(personas)