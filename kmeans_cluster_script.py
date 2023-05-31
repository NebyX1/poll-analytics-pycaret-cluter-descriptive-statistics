#Importamos las librerías y dependencias
import pandas as pd
from pycaret.clustering import *

#Importamos el archivo CSV
df = pd.read_csv('encuesta2019.csv', delimiter=';')

#Creamos un "mapa" con los valores nominales y le indicamos los valores de escala correspondientes para poder trabajar mejor con los clústeres
mapeo_situacion_economica = {
    'Muy Mala': 1,
    'Mala': 2,
    'Regular': 3,
    'Buena': 4,
    'Muy Buena': 5
}

mapeo_nivel_estudios = {
    'Primaria Incompleta': 1,
    'Primaria Completa': 2,
    'Secundaria Incompleta': 3,
    'Secundaria Completa': 4,
    'Terciario Incompleto': 5,
    'Universitario Incompleto': 6,
    'Terciario Completo': 7,
    'Universitario Completo': 8,
    'Posgrado': 9
}

#Aplicamos la transformación mediante mapeo de las columnas seleccionadas para el análisis de clústeres
df['SituaciónEconómica'] = df['SituaciónEconómica'].map(mapeo_situacion_economica)
df['NivelEstudios'] = df['NivelEstudios'].map(mapeo_nivel_estudios)

#Comprobamos que la transformación de los valores de las columnas seleccionadas fue exitosa
print(df[['SituaciónEconómica', 'NivelEstudios']].head())

#Reemplazamos las comas de nuestro ponderador por puntos y convertimos la columna a float(decimales)
df['Ponderador'] = df['Ponderador'].str.replace(',', '.').astype(float)

#Rellenamos todos los valores NaN que puedan existir en nuestro ponderador con el promedio de toda la columna ponderador para no afectar la ponderación
df['Ponderador'] = df['Ponderador'].fillna(df['Ponderador'].mean())

#Creamos un nuevo DataFrame vacío que luego usaremos para multiplicar cada fila según el valor correspondiente en el ponderador
df_ponderado = pd.DataFrame()

#Creamos múltiples instancias de cada fila según su ponderación para tener un análisis verdaderamente representativo de la población medida
for index, row in df.iterrows():
    num_copies = round(row['Ponderador'])
    df_ponderado = df_ponderado.append([row]*num_copies)

#Restablecemos los índices a los valores originales
df_ponderado.reset_index(drop=True, inplace=True)

#Colocamos 'Voto2014' en la primera posición, ya que la primnera columna es la que toma Pycaret como "Feature" de cada punto 
#en nuestro gráfico de clústeres
df_ponderado = df_ponderado[['Voto2014'] + [col for col in df_ponderado.columns if col != 'Voto2014']]

#Configuramos el entorno de pycaret con las columnas el dataframe a analizar, normalizamos los datos y le asignamos un número de id a la sesión
exp_clu = setup(df_ponderado, normalize = True, session_id = 123)

#Creamos el modelo de clústeres, en este caso será bajo el algoritmo de "K-Means" y le indicamos el número de clústeres que debe buscar
kmeans = create_model('kmeans', num_clusters = 3)

#Graficamos el modelo con un tipo de gráfico 3D
plot_model(kmeans, plot = 'tsne')