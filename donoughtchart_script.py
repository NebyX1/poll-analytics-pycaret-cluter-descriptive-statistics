#Importamos las librerías y dependencias
import pandas as pd
import matplotlib.pyplot as plt

#Creamos la función que luego será llamada y ejecutada por streamlit
def plot():
    #Importamos el archivo CSV de la encuesta que vamos a analizar que está en el directorio raíz de este proyecto
    df = pd.read_csv('encuesta2019.csv', delimiter=';')

    #Convertimos el ponderador a números decimales con punto, ya que desde el csv vienen con coma
    df['Ponderador'] = df['Ponderador'].str.replace(',', '.').astype(float)

    #Agrupamos los datos por la columna 'Radio' y sumamos los ponderadores correspondientes a cada encuestado
    grouped = df.groupby('Radio')['Ponderador'].sum()

    #Especificamos los colores con los que queremos que nuestro gráfico pinte cada categoría
    colors = ['skyblue', 'yellowgreen', 'coral', 'gold', 'purple', 'pink', 'orange', 'blue', 'red', 'green']

    #Generamos la gráfica de "dónout" con las etiquetas y le indicamos el tamaño que tendrá
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(grouped, labels = grouped.index, autopct='%1.1f%%', startangle=90, pctdistance=0.85, colors=colors, wedgeprops=dict(width=0.3))

    #Exportamos el gráfico resultante
    return fig