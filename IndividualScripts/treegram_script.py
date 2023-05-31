# Importamos las librerías y dependencias
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Importamos el archivo CSV
df = pd.read_csv('encuesta2019.csv', delimiter=';')

# Convertimos el ponderador a números decimales
df['Ponderador'] = df['Ponderador'].str.replace(',', '.').astype(float)

# Contamos la frecuencia de cada categoría en "AprobaciónPeña"
grouped = df['AprobaciónPeña'].value_counts()

# Calculamos los porcentajes
percentages = grouped / grouped.sum() * 100

# Especificamos los colores
colors = ['skyblue', 'yellowgreen', 'coral', 'gold', 'purple', 'pink', 'orange', 'blue', 'red', 'green']

# Generamos el gráfico de treemap
fig, ax = plt.subplots()
squarify.plot(sizes=percentages, label=percentages.index, color=colors, alpha=.6)

# Creamos las etiquetas con porcentajes
labels = [f"{label}\n{perc:.2f}%" for label, perc in zip(percentages.index, percentages)]

# Generamos el gráfico de treemap con las etiquetas
squarify.plot(sizes=percentages, label=labels, color=colors, alpha=.6)