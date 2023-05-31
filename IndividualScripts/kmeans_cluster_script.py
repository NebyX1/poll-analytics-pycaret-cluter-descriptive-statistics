# Importamos las librerías y dependencias
import pandas as pd
from pycaret.clustering import *

# Importamos el archivo CSV
df = pd.read_csv('encuesta2019.csv', delimiter=';')

# Mapeamos los valores nominales a valores de escala
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

# Aplicamos la transformación
df['SituaciónEconómica'] = df['SituaciónEconómica'].map(mapeo_situacion_economica)
df['NivelEstudios'] = df['NivelEstudios'].map(mapeo_nivel_estudios)

# Comprobamos la transformación
print(df[['SituaciónEconómica', 'NivelEstudios']].head())

# Reemplazamos las comas por puntos y convertimos la columna a float
df['Ponderador'] = df['Ponderador'].str.replace(',', '.').astype(float)

# Rellenar NaN con el promedio
df['Ponderador'] = df['Ponderador'].fillna(df['Ponderador'].mean())

# Crear un nuevo DataFrame vacío
df_ponderado = pd.DataFrame()

# Crear múltiples instancias de cada fila según su ponderación
for index, row in df.iterrows():
    num_copies = round(row['Ponderador'])
    df_ponderado = df_ponderado.append([row]*num_copies)

# Restablecer índices
df_ponderado.reset_index(drop=True, inplace=True)

# Colocamos 'Voto2014' en la primera posición
df_ponderado = df_ponderado[['Voto2014'] + [col for col in df_ponderado.columns if col != 'Voto2014']]

# Configuramos el entorno de pycaret
exp_clu = setup(df_ponderado, normalize = True, session_id = 123)

# Creamos el modelo de clústeres
kmeans = create_model('kmeans', num_clusters = 3)

# Graficamos el modelo
plot_model(kmeans, plot = 'tsne')