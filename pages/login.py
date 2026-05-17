import streamlit as st

st.title("🔐 Autenticação de Usuário")

if "conectado" not in st.session_state:
    st.session_state.conectado = False

if st.session_state.conectado:
    st.success("Você já está conectado!")
    if st.button("Sair"):
        st.session_state.conectado = False
        st.session_state.nivel_acesso = None
        st.rerun()
else:
    aba_login, aba_cadastro = st.tabs(["Login", "Cadastro"])
    
    with aba_login:
        email = st.text_input("E-mail", key="email_login")
        senha = st.text_input("Senha", type="password", key="senha_login")
        
        if st.button("Entrar"):
            # Mock temporário para teste de nível de acesso (RF01)
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
        st.text_input("Nome Completo", key="cad_nome")
        st.text_input("E-mail corporativo/pessoal", key="cad_email")
        st.text_input("Senha", type="password", key="cad_senha")
        st.button("Criar Conta")