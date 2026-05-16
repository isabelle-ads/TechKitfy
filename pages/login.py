import streamlit as st

st.title("🔐 Login")

email = st.text_input("Email")

senha = st.text_input(
    "Senha",
    type="password"
)

if st.button("Entrar"):

    if email == "admin@gmail.com" and senha == "123":

        st.success("Login realizado!")

    else:

        st.error("Email ou senha inválidos")