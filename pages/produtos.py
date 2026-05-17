import streamlit as st

st.title("🛒 Produtos")

st.write("Confira nossos produtos disponíveis.")

st.write("---")

produtos = [

    {
        "nome": "Notebook Gamer",
        "preco": "R$ 5.999",
        "categoria": "Notebook",
        "imagem": "https://images.unsplash.com/photo-1593642702821-c8da6771f0c6"
    },

    {
        "nome": "Mouse RGB",
        "preco": "R$ 199",
        "categoria": "Periférico",
        "imagem": "https://images.unsplash.com/photo-1527814050087-3793815479db"
    },

    {
        "nome": "Monitor 144Hz",
        "preco": "R$ 1.299",
        "categoria": "Monitor",
        "imagem": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf"
    }

]

col1, col2, col3 = st.columns(3)

for i, produto in enumerate(produtos):

    with [col1, col2, col3][i]:

        st.image(
            produto["imagem"],
            use_container_width=True
        )

        st.subheader(produto["nome"])

        st.write(f"💰 {produto['preco']}")

        st.write(f"📦 {produto['categoria']}")

        st.button(
            "Comprar",
            key=i
        )