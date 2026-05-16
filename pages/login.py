import streamlit as st

st.title("🔐 Login")

st.write("Entre com suas credenciais.")

st.write("---")

email = st.text_input(
    "📧 Email"
)

senha = st.text_input(
    "🔑 Senha",
    type="password"
)

lembrar = st.checkbox("Lembrar usuário")

if st.button("Entrar"):

    if email == "admin@gmail.com" and senha == "123":

        st.success("✅ Login realizado com sucesso!")

    else:

        st.error("❌ Email ou senha inválidos")