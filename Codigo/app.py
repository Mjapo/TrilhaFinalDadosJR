import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Visualização de Dados", layout="wide")

# Título da aplicação
st.title("Selecione sua base de Dados")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])

if uploaded_file is not None:
    # Carregar dados
    df = pd.read_csv(uploaded_file)
    
    # Mostrar o DataFrame
    st.subheader("Dados do CSV")
    st.dataframe(df)

    # Selecionar coluna para gerar histograma
    column_name = st.selectbox("Escolha uma coluna para gerar o histograma", df.columns)

    # Gerar e exibir histograma
    if st.button("Gerar Gráfico"):
        fig, ax = plt.subplots()
        df[column_name].hist(ax=ax, bins=30)
        ax.set_title(f'Histograma da {column_name}')
        ax.set_xlabel('Valores')
        ax.set_ylabel('Frequência')
        st.pyplot(fig)

    # Selecionar múltiplas colunas para visualização
    selected_columns = st.multiselect("Escolha as colunas para visualizar", df.columns)

    if selected_columns:
        st.subheader("Visualização das Colunas Selecionadas")
        st.dataframe(df[selected_columns])
