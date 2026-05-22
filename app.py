import streamlit as st
import requests
from utils import carregar_design_premium

# 1. CARREGA O DESIGN PREMIUM DO MENU LATERAL E TEMA ESCURO EM SINTONIA GLOBAL
carregar_design_premium()

# URL base da sua API FastAPI para usuários
API_URL = "http://127.0.0.1:8000/api/usuarios"

# Garante a existência das variáveis de sessão globais
if "conectado" not in st.session_state:
    st.session_state.conectado = False
if "nivel_acesso" not in st.session_state:
    st.session_state.nivel_acesso = None

# ----------------------------------------------------------------------
# CASO 1: USUÁRIO JÁ AUTENTICADO (Visual Limpo de Logout)
# ----------------------------------------------------------------------
if st.session_state.conectado:
    st.write("<br><br>", unsafe_allow_html=True)
    st.success(f"🎉 Sessão Ativa! Você está logado no terminal corporativo como: {st.session_state.nivel_acesso.upper()}")
    
    st.write("<br>", unsafe_allow_html=True)
    if st.button("LOGOUT / DESCONECTAR DO TERMINAL", type="primary", use_container_width=True):
        st.session_state.conectado = False
        st.session_state.nivel_acesso = None
        st.rerun()

# ----------------------------------------------------------------------
# CASO 2: USUÁRIO DESCONECTADO (Exibe a Logo Quadrada Premium + Abas)
# ----------------------------------------------------------------------
else:
    # Injeta a estilização da caixinha da logo quadrada exatamente como no print
    st.markdown("""
        <style>
        .logo-box-container {
            background: linear-gradient(135deg, #111424 0%, #070914 100%);
            border: 1px solid rgba(0, 247, 255, 0.15);
            border-radius: 16px;
            padding: 35px 20px;
            text-align: center;
            max-width: 340px;
            margin: 0 auto 25px auto;
            box-shadow: 0 12px 35px rgba(0,0,0,0.5);
        }
        .logo-lock-icon {
            font-size: 2rem;
            margin-bottom: 10px;
            filter: drop-shadow(0 0 8px rgba(255,200,0,0.4));
        }
        .logo-main-text {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.8rem;
            font-weight: 900;
            color: #ffffff;
            letter-spacing: 3px;
            line-height: 1.2;
        }
        .logo-main-text span {
            color: #00f7ff;
            text-shadow: 0 0 12px rgba(0, 247, 255, 0.6);
        }
        .logo-sub-text {
            color: #66768c;
            font-size: 0.78rem;
            margin-top: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* Ajuste fino nas abas de autenticação */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            justify-content: center;
        }
        .auth-card-wrapper {
            background-color: #0b0f19;
            border: 1px solid rgba(0, 247, 255, 0.1);
            border-radius: 12px;
            padding: 22px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
            margin-top: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Renderização da Logo Centralizada Idêntica ao Mockup
    st.markdown("""
        <div class="logo-box-container">
            <div class="logo-lock-icon">🖲️</div>
            <div class="logo-main-text">TECH<span>KIT</span><br>FY</div>
            <div class="logo-sub-text">Terminal de Autenticação de Dispositivos</div>
        </div>
    """, unsafe_allow_html=True)

    # Divisão das abas operacionais
    aba_login, aba_cadastro = st.tabs(["🔒 Iniciar Sessão Segura", "📝 Cadastrar Operador"])
    
    with aba_login:
        st.markdown('<div class="auth-card-wrapper">', unsafe_allow_html=True)
        email = st.text_input("USUÁRIO / E-MAIL", key="email_login", placeholder="admin@gmail.com")
        senha = st.text_input("CHAVE DE ACESSO", type="password", key="senha_login")
        st.write("<br>", unsafe_allow_html=True)
        
        if st.button("INICIAR SESSÃO SEGURA", type="primary", use_container_width=True):
            if email and senha:
                try:
                    res = requests.post(f"{API_URL}/login", json={"email": email, "senha": senha})
                    if res.status_code == 200:
                        st.session_state.conectado = True
                        
                        if "admin" in email.lower():
                            st.session_state.nivel_acesso = "admin"
                            st.toast("⚡ Modo Administrador liberado.")
                            st.rerun()
                        else:
                            st.session_state.nivel_acesso = "cliente"
                            st.toast("✔️ Usuário autenticado.")
                            # ADICIONADO: Direciona automaticamente o cliente para o catálogo
                            st.switch_page("pages/produtos.py")
                    else:
                        st.error("❌ Credenciais incorretas ou inválidas.")
                except Exception:
                    st.error("❌ Erro ao conectar com o Backend FastAPI. Verifique o Uvicorn!")
            else:
                st.warning("⚠️ Insira o e-mail e a senha.")
        st.markdown('</div>', unsafe_allow_html=True)

    with aba_cadastro:
        st.markdown('<div class="auth-card-wrapper">', unsafe_allow_html=True)
        st.write("Registrar novo colaborador na infraestrutura local:")
        nome_completo = st.text_input("Nome Completo", key="cad_nome")
        email_cadastro = st.text_input("E-mail do Funcionário", key="cad_email")
        senha_cadastro = st.text_input("Definir Nova Senha", type="password", key="cad_senha")
        st.write("<br>", unsafe_allow_html=True)
        
        if st.button("Gravar Ficha Cadastral", use_container_width=True):
            if nome_completo and email_cadastro and senha_cadastro:
                try:
                    res = requests.post(f"{API_URL}/registrar", json={"nome": nome_completo, "email": email_cadastro, "senha": senha_cadastro})
                    if res.status_code == 201:
                        st.session_state.conectado = True
                        
                        if "admin" in email_cadastro.lower():
                            st.session_state.nivel_acesso = "admin"
                            st.toast("⚡ Cadastro Administrador realizado.")
                            st.rerun()
                        else:
                            st.session_state.nivel_acesso = "cliente"
                            st.toast("💾 Conta criada com sucesso!")
                            # ADICIONADO: Direciona automaticamente o cliente para o catálogo logo após registrar
                            st.switch_page("pages/produtos.py")
                    else:
                        st.error(res.json().get("detail", "Erro ao cadastrar."))
                except Exception:
                    st.error("❌ Erro de barramento ao salvar o registro no banco.")
            else:
                st.warning("⚠️ Preencha todos os campos cadastrais.")
        st.markdown('</div>', unsafe_allow_html=True)