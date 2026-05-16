import streamlit as st
import pandas as pd

st.title("🛒 Produtos")

st.write("Lista de produtos disponíveis.")

st.write("---")

dados = {
    "Produto": [
        "Notebook Gamer",
        "Mouse RGB",
        "Monitor 144Hz",
        "Teclado Mecânico"
    ],

    "Preço": [
        "R$ 5.999",
        "R$ 199",
        "R$ 1.299",
        "R$ 350"
    ],

    "Estoque": [
        12,
        30,
        8,
        15
    ]
}

df = pd.DataFrame(dados)

st.dataframe(
    df,
    use_container_width=True
)