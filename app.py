import streamlit as st

st.set_page_config(
    page_title="TechKitfy",
    page_icon="🖥️",
    layout="wide"
)

# SIDEBAR
with st.sidebar:
    st.title("🖥️ TechKitfy")

    st.write("Sistema de Loja Tech")

    pagina = st.radio(
        "Navegação",
        ["Home", "Login", "Produtos"]
    )

# HOME
if pagina == "Home":

    st.title("🚀 Bem-vindo à TechKitfy")

    st.subheader("Sua loja de tecnologia")

    col1, col2, col3 = st.columns(3)

    col1.metric("Produtos", "120")
    col2.metric("Clientes", "85")
    col3.metric("Pedidos", "43")

    st.write("---")

    st.write("Sistema desenvolvido para a disciplina APS.")

# LOGIN
elif pagina == "Login":

    st.title("🔐 Login")

    email = st.text_input("Email")

    senha = st.text_input(
        "Senha",
        type="password"
    )

    if st.button("Entrar"):
        st.success("Login realizado!")

# PRODUTOS
elif pagina == "Produtos":

    st.title("🛒 Produtos")

    produtos = [
        {
            "nome": "Notebook Gamer",
            "preco": "R$ 5.999,00"
        },
        {
            "nome": "Mouse RGB",
            "preco": "R$ 199,00"
        },
        {
            "nome": "Monitor 144Hz",
            "preco": "R$ 1.299,00"
        }
    ]

    st.table(produtos)