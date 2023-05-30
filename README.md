#Proyecto "Poll Analytics with Pycaret Cluter and Descriptive Statistics"

El proyecto "poll-analytics-pycaret-cluter-descriptive-statistics" es un análisis integral de una encuesta política realizada en la provincia de Lavalleja (Uruguay) en setiembre de 2019. Utilizamos estadísticas descriptivas y técnicas de machine learning para explorar varios aspectos de los datos. El archivo de datos "encuesta2019.csv" contiene información demográfica, opiniones políticas, preferencias de voto y más, proporcionando una visión detallada del panorama político de aquel entonces.
La encuesta es verídica y los resultados de la encuesta fueron muy cercanos a la realidad.

A continuación, se describen brevemente los scripts de Python que componen el proyecto.

treegram_script.py
Este script realiza un análisis sobre la columna "AprobaciónPeña" de la encuesta. Esta columna refleja la aprobación del encuestado hacia una figura política llamada Adriana Peña(ex gobernante de la provincia de Lavalleja en Uruguay). Se cuenta la frecuencia de cada categoría (por ejemplo, "Aprueba", "Desaprueba", etc.) y se calculan los porcentajes correspondientes. Se genera un gráfico de treemap que muestra estos porcentajes, lo que facilita la visualización de la distribución de las respuestas​1.

barchart_script.py
El script "barchart_script.py" analiza la columna "InterésEnPolítica", que indica el nivel de interés de los encuestados en la política. Similar al script de treemap, este script cuenta la frecuencia de cada categoría (por ejemplo, "Me gusta mucho", "Me interesa", etc.) y calcula los porcentajes. Se genera un gráfico de barras para visualizar la distribución de las respuestas​.

piechart_script.py
Este script examina la columna "Radio", que indica si el encuestado escucha la radio. Se agrupan los datos por "Radio" y se suman los valores de la columna "Ponderador", que representa el peso de cada encuestado en la muestra. Se genera un gráfico de pastel (o "proyección solar") que muestra la distribución de los encuestados que escuchan y no escuchan la radio​​.

kmeans_cluster_script.py
El script "kmeans_cluster_script.py" utiliza el algoritmo K-means para agrupar a los encuestados en base a su situación económica y nivel de estudios. Primero, se mapean estos valores nominales a una escala numérica. Luego, se rellenan los valores faltantes en la columna "Ponderador" con el promedio. Se crea un nuevo DataFrame en el que cada fila se replica un número de veces igual a su ponderador. Finalmente, se utiliza la librería PyCaret para crear un modelo de agrupación K-means con tres clusters y se genera un gráfico para visualizar los resultados​.