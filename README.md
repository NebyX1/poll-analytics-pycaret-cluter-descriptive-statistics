#Proyecto "Poll Analytics using Pycaret Cluter and Descriptive Statistics with Streamlit"

El proyecto "Poll Analytics using Pycaret Cluter and Descriptive Statistics with Streamlit" es un pipeline de análisis integral de una encuesta política realizada en la provincia de Lavalleja (Uruguay) en setiembre de 2019. Utilizamos estadísticas descriptivas y técnicas de machine learning (clustering) para explorar varios aspectos de los datos. El archivo de datos "encuesta2019.csv" contiene información demográfica, opiniones políticas, preferencias de voto y más, proporcionando una visión detallada del panorama político de aquel entonces.
La encuesta es verídica y los resultados de la encuesta fueron muy cercanos a la realidad.

A continuación, se describen brevemente los scripts de Python que componen el proyecto.

treegram_script.py
Este script realiza un análisis sobre la columna "AprobaciónPeña" de la encuesta. Esta columna refleja la aprobación del encuestado hacia una figura política llamada Adriana Peña(ex gobernante de la provincia de Lavalleja en Uruguay). Se cuenta la frecuencia de cada categoría (por ejemplo, "Aprueba", "Desaprueba", etc.) y se calculan los porcentajes correspondientes. Se genera un gráfico de treemap que muestra estos porcentajes, lo que facilita la visualización de la distribución de las respuestas.

barchart_script.py
El script "barchart_script.py" analiza la columna "InterésEnPolítica", que indica el nivel de interés de los encuestados en la política. Similar al script de treemap, este script cuenta la frecuencia de cada categoría (por ejemplo, "Me gusta mucho", "Me interesa", etc.) y calcula los porcentajes. Se genera un gráfico de barras para visualizar la distribución de las respuestas.

piechart_script.py
En este script, analizamos la "Identificación ideológica" de los encuestados. Todos los datos están agregados por categorías y representados 
gráficamente de acuerdo a su porcentaje. Cabe destacar que se le ha aplicado ponderación, para que los datos sean realmente representativos de la
póblación que estamos queriendo analizar.

donoughtchart_script.py
Similar al script de "barchart", este escript examina la columna "Radio", que indica si el encuestado escucha la radio. Se agrupan los datos por "Radio" y se suman los valores de la columna "Ponderador", que representa el peso de cada encuestado en la muestra. Se genera un gráfico de pastel (o "proyección solar") que muestra la distribución de los encuestados que escuchan y no escuchan la radio.

kmeans_cluster_script.py
El script "kmeans_cluster_script.py" utiliza el algoritmo K-means para agrupar a los encuestados en base a su situación económica y nivel de estudios. Primero, se mapean estos valores nominales a una escala numérica. Luego, se rellenan los valores faltantes en la columna "Ponderador" con el promedio. Se crea un nuevo DataFrame en el que cada fila se replica un número de veces igual a su ponderador. Finalmente, se utiliza la librería PyCaret para crear un modelo de agrupación K-means con tres clusters y se genera un gráfico para visualizar los resultados.

streamlit_script.py
Con Streamlit creamos un pipeline(canalización de procesos de forma sencuencial y automatizada) analítico de producción, el cual va ejecutando cada uno de nuestros scripts para generar un Dashboard estático simple. A pesar de su simpleza, es altamente efectivo para realizar un análisis visual con las estadísticas básicas y descriptivas de algunas de las variables que se encuentran en nuestra encuesta. Adicionalmente, también le hemos añadido la funcionalidad de ejecutar un análisis de clústeres(machine learning no supervisado). Con el fin de descubrir potenciales agrupamientos por variables previamente seleccionadas, de la población que hemos medido.
