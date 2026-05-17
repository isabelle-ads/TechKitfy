import streamlit as st

st.markdown('<div class="main-neon-title">📦 registro patrimonial (ti)</div>', unsafe_allow_html=True)
st.markdown('<div class="main-sub-title">Terminal de cadastramento de ativos eletrônicos de uso interno.</div>', unsafe_allow_html=True)

if "nivel_acesso" not in st.session_state or st.session_state.nivel_acesso != "admin":
    st.error("🔒 Privilégio insuficiente. Esta operação exige credenciais de Administrador Core.")
else:
    st.markdown("""
        <style>
        .form-structural-container {
            background-color: #16162d;
            border: 1px solid rgba(0, 247, 255, 0.1);
            border-radius: 14px;
            padding: 30px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="form-structural-container">', unsafe_allow_html=True)
    with st.form("form_ativos"):
        c1, c2 = st.columns(2)
        with c1:
            eq_nome = st.text_input("NOME COMPLETO DO ATIVO", placeholder="Ex: Servidor PowerEdge R750")
            eq_patrimonio = st.text_input("CÓDIGO DE PATRIMÔNIO (TAG)", placeholder="Ex: BR-TI-8942")
            eq_marca = st.text_input("FABRICANTE / MARCA")
        with c2:
            eq_modelo = st.text_input("MODELO / ESPECIFICAÇÃO")
            eq_setor = st.selectbox("ALOCAÇÃO FÍSICA DO BEM", ["Data Center Local", "Suporte Nível 1", "Financeiro", "Core Team"])
            eq_estado = st.selectbox("STATUS OPERACIONAL", ["Disponível", "Ativo/Em uso", "Manutenção Laboratório"])
            
        st.write("<br>", unsafe_allow_html=True)
        confirmar = st.form_submit_button("CONCLUIR CRUZA DE DADOS (GRAVAR)")
        
        if confirmar:
            if eq_nome and eq_patrimonio:
                st.success(f"💾 Sucesso! Ativo {eq_nome} catalogado sob o registro {eq_patrimonio}.")
            else:
                st.warning("⚠️ Atenção: Os campos de Identificação e Patrimônio não podem ficar nulos.")
    st.markdown('</div>', unsafe_allow_html=True)