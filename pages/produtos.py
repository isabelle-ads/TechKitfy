import streamlit as st

st.title("🛒 TechKitfy - Vitrine de Eletrônicos")
st.subheader("Consulte os produtos disponíveis em nosso catálogo")

# Filtros de busca (Atende ao RF04)
busca = st.text_input("🔍 Pesquisar por nome do produto ou marca:")
categoria = st.selectbox("Filtrar por Categoria", ["Todos", "Notebooks", "Monitores", "Periféricos"])

st.markdown("---")

# Layout de exibição dos cartões de produtos
col1, col2 = st.columns(2)

with col1:
    st.image("https://via.placeholder.com/150", caption="Notebook Gamer High-End")
    st.write("**Modelo:** Nitro V15 | **Marca:** Acer")
    st.write("**Preço:** R$ 4.500,00")
    if st.button("Adicionar ao Carrinho", key="prod_1"):
        st.success("Adicionado!")

with col2:
    st.image("https://via.placeholder.com/150", caption="Monitor UltraWide 29'")
    st.write("**Modelo:** 29UM69G | **Marca:** LG")
    st.write("**Preço:** R$ 1.250,00")
    if st.button("Adicionar ao Carrinho", key="prod_2"):
        st.success("Adicionado!")