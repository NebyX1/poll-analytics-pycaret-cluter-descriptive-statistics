#Importamos todas las librerías y dependencias
import streamlit as st
from treegram_script import plot as treegram_plot
from barchart_script import plot as barchart_plot
from donoughtchart_script import plot as donoughtchart_script
from piechart_script import plot as piechart_script
import subprocess

#Establecemos el nombre de la función que luego pondremos en ejecución(producción)
def main():
    st.markdown("<h1 style='text-align: center; color: white; font-size:45px;'>Dashboard Analítico de Encuesta Lavalleja 2019</h1>", unsafe_allow_html=True)

    #Guardamos los gráficos importados de cada componente que vamos a utilizar
    fig1 = treegram_plot()
    fig2 = barchart_plot()
    fig3 = donoughtchart_script()
    fig4 = piechart_script()

    #?Muestramos los gráficos en el dashboard que vamos a crear aquí, el cual tendrá dos columnas y dos filas, de dos gráficos 
    #?en la parte superior y dos en la parte inferior, más un botón.
    
    #Aquí le indicamos las primeras dos columnas, que en realidad actuarán al mismo tiempo como una sola fila
    col1, col2 = st.columns(2)
    
    #Acá le decimos cual es el gráfico y título (con el formato correspondiente) que debe aparecer en la parte superior izquierda
    with col1:
        st.markdown("<h1 style='text-align: center; color: white; font-size:20px;'>Aprobación Gestión A. Peña</h1>", unsafe_allow_html=True)
        st.pyplot(fig1)

    #Lo mismo que en el anterior, nada más que será respecto al gráfico superior derecho
    with col2:
        st.markdown("<h1 style='text-align: center; color: white; font-size:20px;'>Interés en la Política</h1>", unsafe_allow_html=True)
        st.pyplot(fig2)

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("<h1 style='text-align: center; color: white; font-size:20px;'>¿Escuchan radio?</h1>", unsafe_allow_html=True)
        st.pyplot(fig3)

    with col4:
        st.markdown("<h1 style='text-align: center; color: white; font-size:20px;'>Identificación ideológica</h1>", unsafe_allow_html=True)
        st.pyplot(fig4)
    
    #Aquí creamos un botón en la parte inferior de nuestro Dashboard con el formato de su título y le indicamos que mediante un subprocess 
    #debe ejecutar el script que tenemos con el código para generar un análisis de clústeres
    #!Adicionalmente le indicamos dentro de los "[]" que debe ejecutar este script con el python.exe de nuestro entorno virtual, por lo 
    #!cual se deberá cambiar la dirección del enlace a nuestro propio entorno virtual.
    st.markdown("<h1 style='text-align: center; color: white; font-size:20px;'>Mira los grupos de votantes según nivel de estudios y nivel de ingresos</h1>", unsafe_allow_html=True)
    if st.button('Ver Clústeres'):
        subprocess.run(["C:\\Users\\NebyX\\Documents\\Rescue\\Data Analytics\\Survey Analytics\\venv\\Scripts\\python", "kmeans_cluster_script.py"], check=True)

#Aquí le decimos a Streamlit que debe ejecutar en su servidor la función "main" con la que envolvemos todo nuestro código
if __name__ == "__main__":
    main()