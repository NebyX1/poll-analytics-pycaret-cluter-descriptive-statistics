# Importamos las bibliotecas y dependencias
import pandas as pd
import matplotlib.pyplot as plt

def plot():
    # Importamos el archivo CSV
    df = pd.read_csv('encuesta2019.csv', delimiter=';')

    # Convertimos el ponderador a números decimales
    df['Ponderador'] = df['Ponderador'].str.replace(',', '.').astype(float)

    # Agrupamos por "IdentificaciónIdeológica" y sumamos los ponderadores
    grouped = df.groupby('IdentificaciónIdeológica')['Ponderador'].sum()

    # Calculamos los porcentajes
    percentages = grouped / grouped.sum() * 100

    # Especificamos los colores
    colors = ['skyblue', 'yellowgreen', 'coral', 'gold', 'purple', 'pink', 'orange', 'blue', 'red', 'green']

    # Generamos la gráfica de pastel
    fig, ax = plt.subplots(figsize=(10, 12.4))
    ax.pie(percentages, labels=percentages.index, colors=colors, autopct='%1.1f%%')
    ax.axis('equal')  # Para que la gráfica sea circular

    return fig