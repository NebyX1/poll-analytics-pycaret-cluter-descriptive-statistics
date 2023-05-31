# Importamos las librerías y dependencias
import pandas as pd
import matplotlib.pyplot as plt

# Importamos el archivo CSV
df = pd.read_csv('encuesta2019.csv', delimiter=';')

# Convertimos el ponderador a números decimales
df['Ponderador'] = df['Ponderador'].str.replace(',', '.').astype(float)

# Agrupamos los datos por la columna "Radio" y sumamos ponderador
grouped = df.groupby('Radio')['Ponderador'].sum()

# Especificamos los colores
colors = ['skyblue', 'yellowgreen', 'coral', 'gold', 'purple', 'pink', 'orange', 'blue', 'red', 'green']

# Generamos la gráfica de tipo "proyección solar"
fig, ax = plt.subplots()
ax.pie(grouped, labels = grouped.index, autopct='%1.1f%%', startangle=90, pctdistance=0.85, colors=colors, wedgeprops=dict(width=0.3))