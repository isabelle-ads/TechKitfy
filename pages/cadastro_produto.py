import streamlit as st
import pandas as pd

st.title("📦 Cadastro de Produtos")

st.write("Adicione novos produtos ao sistema.")

st.write("---")

# FORMULÁRIO

nome = st.text_input("Nome do Produto")

preco = st.number_input(
    "Preço",
    min_value=0.0,
    format="%.2f"
)

estoque = st.number_input(
    "Estoque",
    min_value=0,
    step=1
)

categoria = st.selectbox(
    "Categoria",
    [
        "Notebook",
        "Periféricos",
        "Monitor",
        "Smartphone"
    ]
)

descricao = st.text_area(
    "Descrição"
)

# BOTÃO

if st.button("Cadastrar Produto"):

    st.success("✅ Produto cadastrado com sucesso!")

# DADOS MOCKADOS

st.write("---")

st.subheader("📋 Produtos Cadastrados")

dados = {
    "Produto": [
        "Notebook Gamer",
        "Mouse RGB"
    ],

    "Preço": [
        "R$ 5.999",
        "R$ 199"
    ],

    "Categoria": [
        "Notebook",
        "Periféricos"
    ]
}

df = pd.DataFrame(dados)

st.dataframe(
    df,
    use_container_width=True
)