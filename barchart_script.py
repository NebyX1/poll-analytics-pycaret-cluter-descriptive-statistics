# Importamos las librerías y dependencias
import pandas as pd
import matplotlib.pyplot as plt

def plot():
    # Importamos el archivo CSV
    df = pd.read_csv('encuesta2019.csv', delimiter=';')

    # Convertimos el ponderador a números decimales
    df['Ponderador'] = df['Ponderador'].str.replace(',', '.').astype(float)

    # Contamos la frecuencia de cada categoría en "InterésEnPolítica"
    grouped = df['InterésEnPolítica'].value_counts()

    # Calculamos los porcentajes
    percentages = grouped / grouped.sum() * 100

    # Especificamos los colores
    colors = ['skyblue', 'yellowgreen', 'coral', 'gold', 'purple', 'pink', 'orange', 'blue', 'red', 'green']

    # Generamos la gráfica de barras
    fig, ax = plt.subplots(figsize=(7, 6.2))
    bars = ax.bar(percentages.index, percentages, color=colors)
    plt.setp(ax.xaxis.get_label(), visible=True)
    plt.setp(ax.get_xticklabels(), visible=True, rotation=90, ha='right')
    plt.minorticks_off()

    # Ajusta el espacio alrededor de los ejes
    plt.subplots_adjust(bottom=0.2)

    return fig