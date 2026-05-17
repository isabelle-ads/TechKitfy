import streamlit as st

st.title("🔐 Autenticação de Usuário")

# Garante que as variáveis de controle existem
if "conectado" not in st.session_state:
    st.session_state.conectado = False

# Se já estiver logado, mostra opção de sair
if st.session_state.conectado:
    st.success(f"Você já está conectado como: {st.session_state.nivel_acesso.upper()}")
    if st.button("Sair / Logoff"):
        st.session_state.conectado = False
        st.session_state.nivel_acesso = None
        st.rerun()
else:
    aba_login, aba_cadastro = st.tabs(["Login", "Cadastro"])
    
    with aba_login:
        email = st.text_input("E-mail", key="email_login")
        senha = st.text_input("Senha", type="password", key="senha_login")
        
        if st.button("Entrar"):
            # Mock temporário: se o e-mail tiver a palavra "admin", entra como Admin
            if "admin" in email.lower():
                st.session_state.conectado = True
                st.session_state.nivel_acesso = "admin"
                st.success("Login Administrativo efetuado com sucesso!")
            else:
                st.session_state.conectado = True
                st.session_state.nivel_acesso = "cliente"
                st.success("Login Cliente efetuado com sucesso!")
            st.rerun()

    with aba_cadastro:
        st.write("Crie a sua conta para acessar a loja")
        st.text_input("Nome Completo", key="cad_nome")
        st.text_input("E-mail para cadastro", key="cad_email")
        st.text_input("Senha", type="password", key="cad_senha")
        if st.button("Criar Conta"):
            st.success("Conta criada! Alterne para a aba de Login para entrar.")