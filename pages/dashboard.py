import streamlit as st
import requests
# URL base do seu Backend FastAPI para produtos
API_URL = "http://127.0.0.1:8000/api/produtos"

st.markdown('<div class="main-neon-title">📊 telemetria e analytics de ti</div>', unsafe_allow_html=True)
st.markdown('<div class="main-sub-title">Painel executivo de monitoramento de bens e movimentações em tempo real.</div>', unsafe_allow_html=True)

if "nivel_acesso" not in st.session_state or st.session_state.nivel_acesso != "admin":
    st.error("🔒 Área Confidencial. Bloqueio de segurança ativo para usuários não-administradores.")
else:
    # ESTILIZAÇÃO COMPLETA DE ALTO PADRÃO (Estilo SaaS Premium)
    st.markdown("""
        <style>
        /* Cards de KPI */
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
            text-shadow: 0 0 10px rgba(0, 247, 255, 0.3);
        }
        .kpi-description {
            color: #8c97a8;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-top: 8px;
        }
        
        /* Container das Barras por Setor */
        .analytics-box {
            background-color: #16162d;
            border: 1px solid rgba(0, 247, 255, 0.1);
            border-radius: 14px;
            padding: 25px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            margin-top: 20px;
        }
        .sector-row {
            margin-bottom: 18px;
        }
        .sector-label-wrapper {
            display: flex;
            justify-content: space-between;
            font-size: 0.9rem;
            margin-bottom: 6px;
        }
        .sector-name {
            color: #ffffff;
            font-weight: 600;
        }
        .sector-count {
            font-family: 'Orbitron', sans-serif;
            color: #00f7ff;
            font-weight: 700;
        }
        
        /* Barra de progresso customizada fina e moderna */
        .custom-progress-bg {
            background-color: #0f0f1e;
            border-radius: 8px;
            height: 10px;
            width: 100%;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.03);
        }
        .custom-progress-fill {
            background: linear-gradient(90deg, #00b4db 0%, #00f7ff 100%);
            height: 100%;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 247, 255, 0.5);
        }
        </style>
    """, unsafe_allow_html=True)

    # 1. BUSCA OS DADOS REAIS DO BACKEND FASTAPI
    lista_produtos = []
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            lista_produtos = response.json()
    except Exception:
        st.error("❌ Falha de conexão com o servidor FastAPI.")

    # 2. CÁLCULO DAS MÉTRICAS EM TEMPO REAL
    total_ativos = 0
    equipamentos_operantes = 0
    unidades_em_reparo = 0
    setores_distribuicao = {}

    if lista_produtos:
        for produto in lista_produtos:
            qtd = produto.get("quantidade", 1)
            total_ativos += qtd
            
            categoria_str = produto.get("categoria", "")
            setor = "Geral / Não Alocado"
            status_operacional = "Disponível"
            
            if "|" in categoria_str:
                partes = [p.strip() for p in categoria_str.split("|")]
                if len(partes) >= 2:
                    setor = partes[1]
                if len(partes) >= 3:
                    status_operacional = partes[2]
            
            if "manuten" in status_operacional.lower() or "reparo" in status_operacional.lower():
                unidades_em_reparo += qtd
            else:
                equipamentos_operantes += qtd
            
            setores_distribuicao[setor] = setores_distribuicao.get(setor, 0) + qtd

    # 3. RENDERIZAÇÃO DOS CARDS DE KPI
    k1, k2, k3 = st.columns(3)
    with k1:
        st.markdown(f'<div class="kpi-neon-card"><div class="kpi-digit">{total_ativos}</div><div class="kpi-description">Ativos de TI Registrados</div></div>', unsafe_allow_html=True)
    with k2:
        st.markdown(f'<div class="kpi-neon-card" style="border-left-color: #00ffaa;"><div class="kpi-digit">{equipamentos_operantes}</div><div class="kpi-description">Equipamentos Operantes</div></div>', unsafe_allow_html=True)
    with k3:
        st.markdown(f'<div class="kpi-neon-card" style="border-left-color: #ff3b69;"><div class="kpi-digit">{unidades_em_reparo}</div><div class="kpi-description">Unidades em Reparo</div></div>', unsafe_allow_html=True)
        
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("### 📈 Inventário Distribuído por Setor Operacional")
    
    # 4. PAINEL DE ANALYTICS CUSTOMIZADO (SEM PLOTLY GROSSO)
    st.markdown('<div class="analytics-box">', unsafe_allow_html=True)
    
    if not setores_distribuicao or total_ativos == 0:
        st.info("📦 Aguardando inserção de ativos patrimoniais para gerar a volumetria.")
    else:
        # Ordena os setores do que tem mais itens para o que tem menos
        setores_ordenados = sorted(setores_distribuicao.items(), key=lambda x: x[1], reverse=True)
        
        for setor_nome, setor_qtd in setores_ordenados:
            # Calcula a porcentagem real que esse setor ocupa no inventário total
            porcentagem = (setor_qtd / total_ativos) * 100 if total_ativos > 0 else 0
            
            # Gera a linha de progresso fina e elegante via HTML inline
            st.markdown(f"""
                <div class="sector-row">
                    <div class="sector-label-wrapper">
                        <span class="sector-name">📍 {setor_nome}</span>
                        <span class="sector-count">{setor_qtd} un. ({porcentagem:.1f}%)</span>
                    </div>
                    <div class="custom-progress-bg">
                        <div class="custom-progress-fill" style="width: {porcentagem}%;"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
    st.markdown('</div>', unsafe_allow_html=True)