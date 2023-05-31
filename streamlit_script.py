#Importamos todas las librerías y dependencias
import streamlit as st
from treegram_script import plot as treegram_plot
from barchart_script import plot as barchart_plot
from donoughtchart_script import plot as donoughtchart_script
from piechart_script import plot as piechart_script
import subprocess

def main():
    st.markdown("<h1 style='text-align: center; color: white; font-size:45px;'>Dashboard Analítico de Encuesta Lavalleja 2019</h1>", unsafe_allow_html=True)

    # Genera los gráficos
    fig1 = treegram_plot()
    fig2 = barchart_plot()
    fig3 = donoughtchart_script()
    fig4 = piechart_script()

     # Muestra los gráficos en el dashboard
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h1 style='text-align: center; color: white; font-size:20px;'>Aprobación Gestión A. Peña</h1>", unsafe_allow_html=True)
        st.pyplot(fig1)

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
        
    st.markdown("<h1 style='text-align: center; color: white; font-size:20px;'>Mira los grupos de votantes según nivel de estudios y nivel de ingresos</h1>", unsafe_allow_html=True)
    if st.button('Ver Clústeres'):
        subprocess.run(["C:\\Users\\NebyX\\Documents\\Rescue\\Data Analytics\\Survey Analytics\\venv\\Scripts\\python", "kmeans_cluster_script.py"], check=True)
if __name__ == "__main__":
    main()