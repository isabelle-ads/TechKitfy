import streamlit as st

st.title("🔐 Login")

st.write("Bem-vinda à TechKitfy")

st.write("---")

# CENTRALIZAÇÃO

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    email = st.text_input("📧 Email")

    senha = st.text_input(
        "🔑 Senha",
        type="password"
    )

    lembrar = st.checkbox(
        "Lembrar usuário"
    )

    entrar = st.button("Entrar")

    if entrar:

        if email == "admin@gmail.com" and senha == "123":

            st.success(
                "✅ Login realizado!"
            )

        else:

            st.error(
                "❌ Credenciais inválidas"
            )