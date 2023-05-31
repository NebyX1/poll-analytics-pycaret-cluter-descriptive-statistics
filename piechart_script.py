#Importamos las bibliotecas y dependencias
import pandas as pd
import matplotlib.pyplot as plt

#Creamos la función que luego será llamada y ejecutada por streamlit
def plot():
    #Importamos el archivo CSV de la encuesta que vamos a analizar que está en el directorio raíz de este proyecto
    df = pd.read_csv('encuesta2019.csv', delimiter=';')

    #Convertimos el ponderador a números decimales con punto, ya que desde el csv vienen con coma
    df['Ponderador'] = df['Ponderador'].str.replace(',', '.').astype(float)

    #Agrupamos los datos por la columna 'IdentificaciónIdeológica' y sumamos los ponderadores correspondientes a cada encuestado
    grouped = df.groupby('IdentificaciónIdeológica')['Ponderador'].sum()

    #Calculamos los porcentajes de cada categoría existente y lo dividimos entre el total
    percentages = grouped / grouped.sum() * 100

    #Especificamos los colores con los que queremos que nuestro gráfico pinte cada categoría
    colors = ['skyblue', 'yellowgreen', 'coral', 'gold', 'purple', 'pink', 'orange', 'blue', 'red', 'green']

    #Generamos la gráfica de pastel con las etiquetas y le indicamos el tamaño que tendrá
    fig, ax = plt.subplots(figsize=(10, 12.4))
    ax.pie(percentages, labels=percentages.index, colors=colors, autopct='%1.1f%%')
    ax.axis('equal')  # Para que la gráfica sea circular

    #Exportamos el gráfico resultante
    return fig