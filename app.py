import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv("MS_Finan.csv", sep=";")

# Mostrar as primeiras linhas no Streamlit
st.write("### Colunas do DataFrame:")
st.write(df.columns)

# Padronizar nomes das colunas
df.columns = (
    df.columns
    .str.strip()                  # Remove espaços antes/depois
    .str.lower()                  # Converte para minúsculas
    .str.replace(' ', '_')        # Substitui espaços por_
)

# Limpar nomes das colunas (opcional, já feito acima)
df.columns = df.columns.str.strip()

# Contar quantidade de registros por país
count_by_country = df['country'].value_counts()

# Mostrar tabela resumo no Streamlit
st.write("### Quantidade de registros por país:")
st.write(count_by_country)

# Criar gráfico de barras
plt.figure(figsize=(10,6))
count_by_country.plot(kind='bar', color='purple')
plt.title('Quantidade de Registros por País')
plt.xlabel('País')
plt.ylabel('Número de Registros')
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar gráfico no Streamlit
st.pyplot(plt)
