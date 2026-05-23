import streamlit as st
import requests
from utils import carregar_design_premium

# =========================================================
# CONFIG GLOBAL
# =========================================================

carregar_design_premium()

API_URL = "http://127.0.0.1:8000/api/usuarios"

# =========================================================
# SESSION STATE
# =========================================================

if "conectado" not in st.session_state:
    st.session_state.conectado = False

if "nivel_acesso" not in st.session_state:
    st.session_state.nivel_acesso = None

# =========================================================
# SIDEBAR PERSONALIZADA
# =========================================================

st.sidebar.title("🖥️ TERMINAL")

st.sidebar.page_link(
    "app.py",
    label="Home"
)

st.sidebar.page_link(
    "pages/produtos.py",
    label="Produtos"
)

# MENUS ADMIN
if st.session_state.get("nivel_acesso") == "admin":

    st.sidebar.page_link(
        "pages/cadastro_produto.py",
        label="Cadastro Produto"
    )

    st.sidebar.page_link(
        "pages/dashboard.py",
        label="Dashboard"
    )

    st.sidebar.page_link(
        "pages/usuarios.py",
        label="Usuários"
    )

# LOGOUT
if st.session_state.get("conectado"):

    st.sidebar.write("---")

    if st.sidebar.button("🚪 Logout"):

        st.session_state.conectado = False
        st.session_state.nivel_acesso = None

        st.switch_page("app.py")

# =========================================================
# USUÁRIO JÁ LOGADO
# =========================================================

if st.session_state.conectado:

    st.write("<br><br>", unsafe_allow_html=True)

    st.success(
        f"🎉 Sessão ativa como: "
        f"{st.session_state.nivel_acesso.upper()}"
    )

    st.info(
        "Use o menu lateral para navegar pelo sistema."
    )

# =========================================================
# TELA LOGIN
# =========================================================

else:

    # =====================================================
    # CSS
    # =====================================================

    st.markdown("""
        <style>

        .logo-box-container {
            background: linear-gradient(135deg, #111424 0%, #070914 100%);
            border: 1px solid rgba(0, 247, 255, 0.15);
            border-radius: 16px;
            padding: 45px 20px;
            text-align: center;
            max-width: 420px;
            margin: 0 auto 25px auto;
            box-shadow: 0 12px 35px rgba(0,0,0,0.5);
        }

        .logo-main-text {
            font-family: 'Orbitron', sans-serif;
            font-size: 2.7rem;
            font-weight: 900;
            color: #00f7ff;
            text-align: center;
            letter-spacing: 4px;
            text-shadow: 0 0 18px rgba(0,247,255,0.7);
        }

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

# =====================================================
# LOGO
# =====================================================

    st.html("""
            <div style="
                background: linear-gradient(135deg, #111424 0%, #070914 100%);
                border: 1px solid rgba(0, 247, 255, 0.15);
                border-radius: 16px;
                padding: 45px 20px;
                text-align: center;
                max-width: 420px;
                margin: 0 auto 25px auto;
                box-shadow: 0 12px 35px rgba(0,0,0,0.5);
            ">

                <div style="
                    font-family: Arial, sans-serif;
                    font-size: 52px;
                    font-weight: 900;
                    color: #00f7ff;
                    letter-spacing: 4px;
                    text-shadow: 0 0 18px rgba(0,247,255,0.8);
                ">
                    TECHKITFY
                </div>

            </div>
            """)

    # =====================================================
    # ABAS
    # =====================================================

    aba_login, aba_cadastro = st.tabs([
        "🔒 Iniciar Sessão Segura",
        "📝 Cadastrar Operador"
    ])

    # =====================================================
    # LOGIN
    # =====================================================

    with aba_login:

        st.markdown(
            '<div class="auth-card-wrapper">',
            unsafe_allow_html=True
        )

        email = st.text_input(
            "USUÁRIO / E-MAIL",
            key="email_login",
            placeholder="admin@gmail.com"
        )

        senha = st.text_input(
            "CHAVE DE ACESSO",
            type="password",
            key="senha_login"
        )

        st.write("<br>", unsafe_allow_html=True)

        if st.button(
            "INICIAR SESSÃO SEGURA",
            type="primary",
            use_container_width=True
        ):

            if email and senha:

                try:

                    res = requests.post(
                        f"{API_URL}/login",
                        json={
                            "email": email,
                            "senha": senha
                        }
                    )

                    if res.status_code == 200:

                        st.session_state.conectado = True

                        # ADMIN
                        if "admin" in email.lower():

                            st.session_state.nivel_acesso = "admin"

                            st.toast(
                                "⚡ Modo Administrador liberado."
                            )

                            st.rerun()

                        # CLIENTE
                        else:

                            st.session_state.nivel_acesso = "cliente"

                            st.toast(
                                "✔️ Usuário autenticado."
                            )

                            st.switch_page(
                                "pages/produtos.py"
                            )

                    else:

                        st.error(
                            "❌ Credenciais incorretas."
                        )

                except Exception:

                    st.error(
                        "❌ Backend FastAPI offline."
                    )

            else:

                st.warning(
                    "⚠️ Preencha e-mail e senha."
                )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    # =====================================================
    # CADASTRO
    # =====================================================

    with aba_cadastro:

        st.markdown(
            '<div class="auth-card-wrapper">',
            unsafe_allow_html=True
        )

        st.write(
            "Registrar novo colaborador:"
        )

        nome_completo = st.text_input(
            "Nome Completo",
            key="cad_nome"
        )

        email_cadastro = st.text_input(
            "E-mail",
            key="cad_email"
        )

        senha_cadastro = st.text_input(
            "Senha",
            type="password",
            key="cad_senha"
        )

        st.write("<br>", unsafe_allow_html=True)

        if st.button(
            "Gravar Ficha Cadastral",
            use_container_width=True
        ):

            if (
                nome_completo
                and email_cadastro
                and senha_cadastro
            ):

                try:

                    res = requests.post(
                        f"{API_URL}/registrar",
                        json={
                            "nome": nome_completo,
                            "email": email_cadastro,
                            "senha": senha_cadastro
                        }
                    )

                    if res.status_code == 201:

                        st.session_state.conectado = True

                        if "admin" in email_cadastro.lower():

                            st.session_state.nivel_acesso = "admin"

                            st.toast(
                                "⚡ Cadastro Admin realizado."
                            )

                            st.rerun()

                        else:

                            st.session_state.nivel_acesso = "cliente"

                            st.toast(
                                "💾 Conta criada com sucesso!"
                            )

                            st.switch_page(
                                "pages/produtos.py"
                            )

                    else:

                        st.error(
                            res.json().get(
                                "detail",
                                "Erro ao cadastrar."
                            )
                        )

                except Exception:

                    st.error(
                        "❌ Falha ao salvar no banco."
                    )

            else:

                st.warning(
                    "⚠️ Preencha todos os campos."
                )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )