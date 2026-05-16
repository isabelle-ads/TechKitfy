import streamlit as st

st.title("🛒 Produtos")

produtos = [
    {
        "Produto": "Notebook Gamer",
        "Preço": "R$ 5.999"
    },
    {
        "Produto": "Mouse RGB",
        "Preço": "R$ 199"
    },
    {
        "Produto": "Monitor 144Hz",
        "Preço": "R$ 1.299"
    }
]

st.table(produtos)