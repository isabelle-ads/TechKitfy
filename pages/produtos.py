import streamlit as st
import pandas as pd

# ESTADO DA SESSÃO

if "produtos" not in st.session_state:

    st.session_state.produtos = [

        {
            "nome": "Notebook Gamer",
            "preco": 5999,
            "categoria": "Notebook"
        },

        {
            "nome": "Mouse RGB",
            "preco": 199,
            "categoria": "Periférico"
        }

    ]

# TÍTULO

st.title("🛒 Produtos")

st.write("Gerencie os produtos da TechKitfy.")

st.write("---")

# FORMULÁRIO

st.subheader("📦 Adicionar Produto")

col1, col2 = st.columns(2)

with col1:

    nome = st.text_input("Nome do Produto")

    preco = st.number_input(
        "Preço",
        min_value=0.0,
        format="%.2f"
    )

with col2:

    categoria = st.selectbox(
        "Categoria",
        [
            "Notebook",
            "Periférico",
            "Monitor",
            "Smartphone"
        ]
    )

# BOTÃO

if st.button("Cadastrar Produto"):

    novo_produto = {

        "nome": nome,
        "preco": preco,
        "categoria": categoria
    }

    st.session_state.produtos.append(
        novo_produto
    )

    st.success("✅ Produto cadastrado!")

st.write("---")

# LISTAGEM

st.subheader("📋 Lista de Produtos")

for i, produto in enumerate(
    st.session_state.produtos
):

    col1, col2, col3, col4 = st.columns(
        [3, 2, 2, 1]
    )

    col1.write(produto["nome"])

    col2.write(
        f"R$ {produto['preco']}"
    )

    col3.write(
        produto["categoria"]
    )

    # EXCLUIR

    if col4.button(
        "🗑️",
        key=i
    ):

        st.session_state.produtos.pop(i)

        st.rerun()