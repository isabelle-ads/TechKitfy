import streamlit as st
import requests
from utils import carregar_design_premium

# EXECUTA ELA LOGO NA PRIMEIRA LINHA DE CÓDIGO
carregar_design_premium()
# URL da sua API FastAPI para produtos
API_URL = "http://127.0.0.1:8000/api/produtos"

# No topo do seu pages/cadastro_produto.py substitua os st.title/st.write antigos por:
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
            eq_marca = st.text_input("FABRICANTE / MARCA", placeholder="Ex: Akko, Dell, LG")
            eq_preco = st.number_input("VALOR ESTIMADO DO ATIVO (R$)", min_value=0.0, value=0.0, step=50.0)
        with c2:
            eq_modelo = st.text_input("MODELO / ESPECIFICAÇÃO", placeholder="Ex: TAC75 Magnetic Switch")
            eq_setor = st.selectbox("ALOCAÇÃO FÍSICA DO BEM", ["Data Center Local", "Suporte Nível 1", "Financeiro", "Core Team"])
            eq_estado = st.selectbox("STATUS OPERACIONAL", ["Disponível", "Ativo/Em uso", "Manutenção Laboratório"])
            eq_qtd = st.number_input("QUANTIDADE EM ESTOQUE", min_value=1, value=1, step=1)
            
        st.write("<br>", unsafe_allow_html=True)
        
        # O CAMPO MÁGICO: Agora você cola o link da foto direto pelo site!
        eq_imagem = st.text_input("🔗 URL DA IMAGEM DO ATIVO", placeholder="Cole o link da foto da internet aqui...")
        
        st.write("<br>", unsafe_allow_html=True)
        confirmar = st.form_submit_button("CONCLUIR CRUZA DE DADOS (GRAVAR)")
        
        if confirmar:
            if eq_nome and eq_patrimonio:
                # Organiza os dados para enviar ao banco
                nome_composto = f"{eq_nome} ({eq_modelo})" if eq_modelo else eq_nome
                categoria_composta = f"{eq_marca} | {eq_setor} | {eq_estado}"
                
                # Se não colar imagem, o sistema usa a do teclado como padrão automática
                foto_final = eq_imagem.strip() if eq_imagem.strip() != "" else "https://ae-pic-a1.aliexpress-media.com/kf/Sec5692edf0554298a37a89db4fa740d4o.jpg_220x220q75.jpg"
                
                payload = {
                    "nome": nome_composto,
                    "categoria": categoria_composta,
                    "preco": float(eq_preco),
                    "quantidade": int(eq_qtd),
                    "imagem_url": foto_final
                }
                
                try:
                    res = requests.post(API_URL, json=payload)
                    
                    if res.status_code == 201:
                        st.success(f"💾 Sucesso! Ativo {eq_nome} catalogado e integrado ao banco SQLite.")
                        st.balloons()
                    else:
                        st.error(f"❌ Erro na validação do banco. Status: {res.status_code}")
                except Exception:
                    st.error("❌ Erro de conexão. O servidor Backend FastAPI (Uvicorn) está ligado?")
            else:
                st.warning("⚠️ Atenção: Os campos de Identificação e Patrimônio não podem ficar nulos.")
    st.markdown('</div>', unsafe_allow_html=True)