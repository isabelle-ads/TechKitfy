import streamlit as st

st.markdown("""
    <style>
    .login-wrapper {
        background: linear-gradient(135deg, rgba(22, 22, 45, 0.7) 0%, rgba(15, 15, 30, 0.85) 100%);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 247, 255, 0.2);
        border-radius: 20px;
        padding: 45px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6), 0 0 30px rgba(0, 247, 255, 0.1);
        text-align: center;
        margin-top: 5vh;
    }
    .auth-badge {
        font-family: "Orbitron", sans-serif;
        font-size: 2.3rem;
        color: #ffffff;
        font-weight: 900;
        letter-spacing: 3px;
        margin-bottom: 5px;
    }
    .auth-badge span {
        color: #00f7ff;
        text-shadow: 0 0 15px #00f7ff;
    }
    </style>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns([1, 1.6, 1])

with c2:
    st.markdown("""
        <div class="login-wrapper">
            <div class="auth-badge">🔐 TECH<span>KITFY</span></div>
            <div style="color: #8c97a8; font-size: 0.9rem; margin-bottom: 25px;">Terminal de Autenticação de Dispositivos</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    email = st.text_input("USUÁRIO / E-MAIL", placeholder="admin@gmail.com")
    senha = st.text_input("CHAVE DE ACESSO", type="password", placeholder="••••••••")
    
    st.write("")
    # Botão com comportamento estendido em largura
    if st.button("INICIAR SESSÃO SEGURA", use_container_width=True, type="primary"):
        if email == "admin@gmail.com" and senha == "123":
            st.session_state.conectado = True
            st.session_state.nivel_acesso = "admin"
            st.success("🔓 Permissão concedida. Carregando os módulos administrativos...")
            st.rerun()
        elif email != "" and senha != "":
            st.session_state.conectado = True
            st.session_state.nivel_acesso = "cliente"
            st.success("🔓 Acesso Cliente liberado!")
            st.rerun()
        else:
            st.error("❌ Falha na consistência de dados. Preencha os campos corporativos.")