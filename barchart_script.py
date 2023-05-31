#Importamos las librerías y dependencias
import pandas as pd
import matplotlib.pyplot as plt

#Creamos la función que luego será llamada y ejecutada por streamlit
def plot():
    #Importamos el archivo CSV de la encuesta que vamos a analizar que está en el directorio raíz de este proyecto
    df = pd.read_csv('encuesta2019.csv', delimiter=';')

    #Convertimos el ponderador a números decimales con punto, ya que desde el csv vienen con coma
    df['Ponderador'] = df['Ponderador'].str.replace(',', '.').astype(float)

    #Agrupamos los datos por la columna 'InterésEnPolítica' y sumamos los ponderadores correspondientes a cada encuestado
    grouped = df.groupby('InterésEnPolítica')['Ponderador'].sum()

    #Calculamos los porcentajes de cada categoría existente y lo dividimos entre el total
    percentages = grouped / grouped.sum() * 100

    #Especificamos los colores con los que queremos que nuestro gráfico pinte cada categoría
    colors = ['skyblue', 'yellowgreen', 'coral', 'gold', 'purple', 'pink', 'orange', 'blue', 'red', 'green']

    #Generamos la gráfica de barras con las etiquetas y le indicamos el tamaño que tendrá
    fig, ax = plt.subplots(figsize=(7, 6.2))
    bars = ax.bar(percentages.index, percentages, color=colors)
    
    # Agregamos las etiquetas de porcentaje a las barras
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{round(yval, 2)}%', ha='center', va='bottom')

    #Acá le indicamos que las etiquetas inferiores que marcan las categorías deberán aparecer rotadas 90 grados
    plt.setp(ax.xaxis.get_label(), visible=True)
    plt.setp(ax.get_xticklabels(), visible=True, rotation=90, ha='right')
    plt.minorticks_off()

    #Esto ajusta el espacio alrededor de los ejes
    plt.subplots_adjust(bottom=0.2)

    #Exportamos el gráfico resultante
    return fig