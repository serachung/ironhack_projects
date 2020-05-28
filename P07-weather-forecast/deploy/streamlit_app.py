import streamlit as st
import pandas as pd
import plotly_express as px
import seaborn as sns

#Para rodar localmente ir na pasta do arquivo através do cmd e dar o comando streamlit run app.py

df_raw = (pd.read_csv)("../data/rain_data_aus.csv")
df_process = df_raw.copy()

def capa():
    st.header('Aleatório == Luis')


def visaogeralpa():
    st.header('** Exploração dos dados **')
    set_data = st.selectbox('Escolha a base de dados que deseja selecionar:', ('Raw data', 'Process data'))
    df = df_raw if set_data == 'Raw data' else df_process
    st.subheader("**Informações sobre o dataset:**")
    st.markdown("Total de Linhas: " + str(df.shape[0]))
    st.markdown("Total de Colunas: " + str(df.shape[1]))

    st.subheader("**Visualização do dataset:**")
    linhas = st.slider('Quantidade de linhas para visualizar', min_value=1, max_value=20, value=5)
    st.dataframe(df.head(linhas))

    st.subheader("**Estrutura do dataset:**")
    expl = pd.DataFrame({
        'TIPO': df.dtypes,
        'NAN': df.isna().sum(),
        'NAN %': (df.isna().sum() / df.shape[0]) * 100
    })
    st.dataframe(expl)

def analise_dados():
    st.header('** Análise das variavéis categoricas**')
    st.subheader('Rainfall x Location')
    df_process.dropna(inplace=True) # quebra galho retirar
    cities_lst = list(df_process['location'].unique())
    cities = st.multiselect('Escolha as cidades que deseja ver os dados', cities_lst,default=cities_lst)
    df_filter = df_process[(df_process['location'].isin(cities))]
    soma_local = df_filter.groupby('location')['location','rainfall'].sum().reset_index()
    soma_local = soma_local.sort_values(by='rainfall')
    fig=px.bar(soma_local,x='location',y='rainfall')
    st.plotly_chart(fig)


def main():

    add_selectbox = st.sidebar.selectbox(
        'Dados para apresentação:',
        ('Capa', 'Visão Geral dos Dados','Análise variavéis categoricas'))

    if add_selectbox == 'Capa':
        capa()


    elif add_selectbox == 'Visão Geral dos Dados':
        visaogeralpa()

    elif add_selectbox == 'Análise variavéis categoricas':
        analise_dados()





if __name__ == '__main__':
    main()