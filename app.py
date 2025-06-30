
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Autoevaluación y Plan de Carrera", layout="wide")

@st.cache_data
def load_data():
    file_path = "Valoracion_Jobs.xlsx"
    df_comp = pd.read_excel(file_path, sheet_name="Competencias Agrupadas")
    df_beh = pd.read_excel(file_path, sheet_name="Comportamientos")
    return df_comp, df_beh

df_comp, df_beh = load_data()

st.title("Autoevaluación de Competencias y Plan de Carrera")

st.write("Archivo cargado correctamente con las siguientes hojas:")
st.write("- Competencias Agrupadas")
st.write("- Comportamientos")
