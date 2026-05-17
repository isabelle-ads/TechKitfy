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

st.write("---")

st.subheader("🛍️ Produtos Disponíveis")

pesquisa = st.text_input(
    "🔍 Pesquisar produto"
)

filtro_categoria = st.selectbox(
    "📂 Filtrar Categoria",
    [
        "Todas",
        "Notebook",
        "Periférico",
        "Monitor",
        "Smartphone"
    ]
)

colunas = st.columns(3)

for i, produto in enumerate(st.session_state.produtos):

    if pesquisa.lower() not in produto["nome"].lower():

        continue

    if filtro_categoria != "Todas":

        if produto["categoria"] != filtro_categoria:

            continue

    with colunas[i % 3]:

        st.container(border=True)

        st.image(
            "https://images.unsplash.com/photo-1517336714739-489689fd1ca8",
            use_container_width=True
        )

        st.subheader(produto["nome"])

        st.write(f"💰 R$ {produto['preco']}")

        st.write(f"📦 {produto['categoria']}")

        if st.button(
            "🗑️ Excluir",
            key=i
        ):

            st.session_state.produtos.pop(i)

            st.rerun()