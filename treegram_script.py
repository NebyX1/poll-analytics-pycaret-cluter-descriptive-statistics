#Importamos las librerías y dependencias
import pandas as pd
import matplotlib.pyplot as plt
import squarify

#Creamos la función que luego será llamada y ejecutada por streamlit
def plot():
    #Importamos el archivo CSV de la encuesta que vamos a analizar que está en el directorio raíz de este proyecto
    df = pd.read_csv('encuesta2019.csv', delimiter=';')

    #Convertimos el ponderador a números decimales con punto, ya que desde el csv vienen con coma
    df['Ponderador'] = df['Ponderador'].str.replace(',', '.').astype(float)

    #Agrupamos los datos por la columna 'AprobaciónPeña' y sumamos los ponderadores correspondientes a cada encuestado
    grouped = df.groupby('AprobaciónPeña')['Ponderador'].sum()

    #Calculamos los porcentajes de cada categoría existente y lo dividimos entre el total
    percentages = grouped / grouped.sum() * 100

    #Especificamos los colores con los que queremos que nuestro gráfico pinte cada categoría
    colors = ['skyblue', 'yellowgreen', 'coral', 'gold', 'purple', 'pink', 'orange', 'blue', 'red', 'green']

    #Creamos las etiquetas con los porcentajes correspondientes
    labels = [f"{label}\n{perc:.2f}%" for label, perc in zip(percentages.index, percentages)]

    #Generamos el gráfico de treemap(rectángulos) con las etiquetas y le indicamos el tamaño que tendrá
    fig, ax = plt.subplots(figsize=(7, 7))
    squarify.plot(sizes=percentages, label=labels, color=colors, alpha=.6)

    #Exportamos el gráfico resultante
    return fig