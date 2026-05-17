import streamlit as st

st.markdown('<div class="main-neon-title">📊 telemetria e analytics de ti</div>', unsafe_allow_html=True)
st.markdown('<div class="main-sub-title">Painel executivo de monitoramento de bens e movimentações em tempo real.</div>', unsafe_allow_html=True)

if "nivel_acesso" not in st.session_state or st.session_state.nivel_acesso != "admin":
    st.error("🔒 Área Confidencial. Bloqueio de segurança ativo para usuários não-administradores.")
else:
    st.markdown("""
        <style>
        .kpi-neon-card {
            background: linear-gradient(135deg, #16162d 0%, #0c0c1a 100%);
            border-left: 5px solid #00f7ff;
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.4);
            text-align: center;
        }
        .kpi-digit {
            font-family: 'Orbitron', sans-serif;
            font-size: 2.2rem;
            font-weight: 900;
            color: #ffffff;
            text-shadow: 0 0 10px rgba(255,255,255,0.1);
        }
        .kpi-description {
            color: #8c97a8;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-top: 8px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Grid de KPIs estruturados
    k1, k2, k3 = st.columns(3)
    
    with k1:
        st.markdown('<div class="kpi-neon-card"><div class="kpi-digit">154</div><div class="kpi-description">Ativos de TI Registrados</div></div>', unsafe_allow_html=True)
    with k2:
        st.markdown('<div class="kpi-neon-card" style="border-left-color: #00ffaa;"><div class="kpi-digit">142</div><div class="kpi-description">Equipamentos Operantes</div></div>', unsafe_allow_html=True)
    with k3:
        st.markdown('<div class="kpi-neon-card" style="border-left-color: #ff3b69;"><div class="kpi-digit">12</div><div class="kpi-description">Unidades em Reparo</div></div>', unsafe_allow_html=True)
        
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("### 📈 Inventário Distribuído por Setor Operacional")
    
    # Massa de dados mapeada
    dataset = {"TI Interno": 45, "Suporte": 35, "Financeiro": 20, "RH": 15, "Estoque": 39}
    
    # Gráfico nativo absorvendo a cor exata do neon digital da sua aplicação
    st.bar_chart(dataset, color="#00f7ff")