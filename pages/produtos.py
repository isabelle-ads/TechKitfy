import streamlit as st
import requests
import urllib.parse
from utils import carregar_design_premium

import streamlit as st

# ==================================================
# SIDEBAR GLOBAL
# ==================================================

st.sidebar.title("🖥️ TERMINAL")

st.sidebar.page_link(
    "app.py",
    label="Home"
)

st.sidebar.page_link(
    "pages/produtos.py",
    label="Produtos"
)

# ADMIN
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

# EXECUTA A UNIFICAÇÃO DO DESIGN DO MENU LATERAL E TEMA ESCURO
carregar_design_premium()

# URL base do seu Backend FastAPI para produtos
API_URL = "http://127.0.0.1:8000/api/produtos"

# LINK DIRETO DO SEU GRUPO DO WHATSAPP
LINK_GRUPO_WHATSAPP = "https://chat.whatsapp.com/CYpVtXlomitKjEvIMfCiVO"

# Inicialização do carrinho na sessão caso seja um acesso cliente
if "carrinho" not in st.session_state:
    st.session_state.carrinho = {}

def carregar_estilo_premium():
    st.markdown("""
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Orbitron:wght@400..900&display=swap" rel="stylesheet">
        
        <style>
        html, body, [data-testid="stAppViewContainer"] {
            font-family: "Montserrat", sans-serif;
            background-color: #0d1117 !important;
        }
        
        .neon-title { font-family: "Orbitron", sans-serif; color: #00f7ff; text-shadow: 0 0 15px rgba(0, 247, 255, 0.6); font-weight: 900; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px; font-size: 2.2rem; }
        .sub-neon { color: #8c97a8; font-size: 0.95rem; margin-bottom: 30px; }
        
        /* CARD INTEGRADO REDIMENSIONADO PARA GRID NATIVO */
        .tech-card {
            background-color: #0b0f19;
            border: 2px solid #00f7ff;
            border-radius: 12px;
            padding: 14px;
            text-align: center;
            box-shadow: 0 0 12px rgba(0, 247, 255, 0.25);
            width: 100%;
            height: 380px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            box-sizing: border-box;
            margin-bottom: 5px;
        }
        
        .tech-card:hover { transform: translateY(-5px); box-shadow: 0 0 25px rgba(0, 247, 255, 0.55); background-color: #111726; }
        .product-image-container img { width: 100%; height: 130px; object-fit: cover; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.05); }
        .card-info-block { text-align: left; margin-top: 8px; }
        .prod-name { font-family: "Montserrat", sans-serif; font-weight: 700; font-size: 0.9rem; color: #ffffff; line-height: 1.3; height: 36px; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; }
        .prod-category { font-family: "Montserrat", sans-serif; font-size: 0.75rem; color: #00f7ff; margin-top: 3px; font-weight: 600; text-transform: uppercase; }
        .price-stock-row { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 8px; margin-top: 5px; }
        .prod-price-tag { font-family: "Orbitron", sans-serif; font-size: 1.1rem; font-weight: 800; color: #00f7ff; }
        .prod-stock-tag { font-family: "Orbitron", sans-serif; color: #8c97a8; font-size: 0.85rem; font-weight: 700; }
        .card-actions-row { display: flex; gap: 8px; margin-top: 12px; width: 100%; }
        .btn-card-action { flex: 1; text-decoration: none; padding: 6px 0; font-size: 0.78rem; font-weight: 700; border-radius: 6px; text-align: center; display: inline-block; transition: all 0.2s ease; }
        .btn-edit { border: 1px solid #00f7ff; color: #00f7ff; background: rgba(0, 247, 255, 0.03); }
        .btn-edit:hover { background: #00f7ff; color: #0b0f19; box-shadow: 0 0 8px rgba(0, 247, 255, 0.4); }
        .btn-delete { border: 1px solid #ff3b3b; color: #ff3b3b; background: rgba(255, 59, 59, 0.03); }
        .btn-delete:hover { background: #ff3b3b; color: #ffffff; box-shadow: 0 0 8px rgba(255, 59, 59, 0.4); }
        .form-overlay-box { background-color: #111726; border: 2px solid #00f7ff; border-radius: 12px; padding: 20px; margin-top: 20px; box-shadow: 0 0 20px rgba(0, 247, 255, 0.2); }
        .cart-overlay-box { background: linear-gradient(135deg, #111b24 0%, #0b0f19 100%); border: 2px solid #00ffaa; border-radius: 12px; padding: 20px; margin-bottom: 25px; box-shadow: 0 0 15px rgba(0, 255, 170, 0.2); }
        div.stButton > button { margin-top: 0px !important; }
        </style>
    """, unsafe_allow_html=True)

carregar_estilo_premium()

# Controle de nível de acesso
eh_admin = "nivel_acesso" in st.session_state and st.session_state.nivel_acesso == "admin"

st.markdown('<div class="neon-title">TechKitfy Stock</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-neon">Catálogo | Ativos eletrônicos integrados ao banco de dados corporativo.</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------
# INTERFACE DO CARRINHO DE COMPRAS
# ----------------------------------------------------------------------
if not eh_admin and st.session_state.carrinho:
    st.markdown("""
        <style>
        div[data-testid="stTextArea"] textarea { background-color: #070914 !important; color: #00ffaa !important; font-family: monospace !important; border: 1px solid rgba(0, 255, 170, 0.2) !important; border-radius: 8px !important; font-size: 0.9rem !important; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="cart-overlay-box">', unsafe_allow_html=True)
    st.markdown("<h4 style='color: #00ffaa; font-family: Orbitron; margin-bottom: 15px;'>🛍️ Sacola de Pedidos</h4>", unsafe_allow_html=True)
    
    total_pedido = 0.0
    texto_recibo = "🛒 *NOVO PEDIDO - TECHKITFY STOCK*\n\n"
    texto_recibo += "Olá, equipe! Gostaria de confirmar os seguintes ativos da minha sacola:\n\n"
    
    for nome_c, dados_c in list(st.session_state.carrinho.items()):
        subtotal = dados_c["preco"] * dados_c["qtd"]
        total_pedido += subtotal
        st.write(f"🔹 **{nome_c}** — {dados_c['qtd']} un. x R$ {dados_c['preco']:.2f} (`R$ {subtotal:.2f}`)")
        texto_recibo += f"• {dados_c['qtd']}x {nome_c} (R$ {dados_c['preco']:.2f} cada)\n"
        
    texto_recibo += f"\n*Valor Total:* R$ {total_pedido:.2f}"
    st.write(f"### Total: R$ {total_pedido:.2f}")
    
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("<p style='color: #8c97a8; font-size: 0.85rem; margin-bottom: 5px;'>📋 <strong>PASSO 1:</strong> Toque no botão de copiar no canto superior direito do recibo:</p>", unsafe_allow_html=True)
    
    st.text_area(label="Recibo", value=texto_recibo, height=180, label_visibility="collapsed", key="recibo_box")
    
    st.markdown("<p style='color: #8c97a8; font-size: 0.85rem; margin-top: 15px; margin-bottom: 5px;'>➡️ <strong>PASSO 2:</strong> Clique abaixo para ir ao grupo e colar o texto:</p>", unsafe_allow_html=True)
    
    w1, w2 = st.columns([3, 1])
    with w1:
        st.link_button("🟢 ABRIR GRUPO DO WHATSAPP", LINK_GRUPO_WHATSAPP, use_container_width=True)
    with w2:
        if st.button("Limpar Sacola", use_container_width=True):
            st.session_state.carrinho = {}
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# PROCESSA PARAMETROS URL
query_params = st.query_params
if "action" in query_params and "id" in query_params:
    acao = query_params["action"]
    prod_id = int(query_params["id"])
    if acao == "editar":
        st.session_state.produto_editar = prod_id
        if "produto_deletar" in st.session_state: del st.session_state.produto_deletar
    elif acao == "deletar":
        st.session_state.produto_deletar = prod_id
        if "produto_editar" in st.session_state: del st.session_state.produto_editar
    st.query_params.clear()

# BUSCA OS PRODUTOS
lista_produtos = []
try:
    response = requests.get(API_URL)
    if response.status_code == 200:
        lista_produtos = response.json()
except Exception:
    st.error("❌ Falha de conexão com o backend FastAPI.")

if not lista_produtos:
    st.info("📦 Nenhum ativo patrimonial cadastrado no banco SQLite.")
else:
    # 🌟 A MÁGICA DO GRID NATIVO: Desenha as colunas em blocos de 4
    num_colunas = 4
    for i in range(0, len(lista_produtos), num_colunas):
        linha_atual = lista_produtos[i:i+num_colunas]
        cols = st.columns(num_colunas)
        
        for j, produto in enumerate(linha_atual):
            with cols[j]:
                img_url = produto.get("imagem_url") or "https://ae-pic-a1.aliexpress-media.com/kf/Sec5692edf0554298a37a89db4fa740d4o.jpg_220x220q75.jpg"
                marca_limpa = produto['categoria'].split('|')[0].strip() if '|' in produto['categoria'] else produto['categoria']
                
                botoes_card = ""
                if eh_admin:
                    botoes_card = f'<div class="card-actions-row"><a href="?action=editar&id={produto["id"]}" target="_self" class="btn-card-action btn-edit">✏️ Editar</a><a href="?action=deletar&id={produto["id"]}" target="_self" class="btn-card-action btn-delete">🗑️ Apagar</a></div>'
                
                html_bruto = f"""
                <div class="tech-card">
                    <div>
                        <div class="product-image-container"><img src="{img_url}"></div>
                        <div class="card-info-block">
                            <div class="prod-name">{produto['nome']}</div>
                            <div class="prod-category">🔹 {marca_limpa}</div>
                        </div>
                    </div>
                    <div>
                        <div class="price-stock-row">
                            <div class="prod-price-tag">R$ {produto['preco']:.2f}</div>
                            <div class="prod-stock-tag">x{produto['quantidade']}</div>
                        </div>
                        {botoes_card}
                    </div>
                </div>
                """
                
                # 💉 VACINA ANTI-MARKDOWN: Arranca todas as quebras de linha e recuos
                html_blindado = html_bruto.replace("\n", "").replace("    ", "")
                st.markdown(html_blindado, unsafe_allow_html=True)
                
                if not eh_admin:
                    if st.button("🛍️ Adicionar ao Pedido", key=f"add_cart_{produto['id']}", use_container_width=True):
                        p_nome = produto['nome']
                        if p_nome in st.session_state.carrinho:
                            st.session_state.carrinho[p_nome]["qtd"] += 1
                        else:
                            st.session_state.carrinho[p_nome] = {"preco": produto['preco'], "qtd": 1}
                        st.toast(f"🛒 {p_nome} inserido na sacola!")
                        st.rerun()

    # --- PROCESSAMENTO DOS FORMULÁRIOS INFERIORES ---
    for produto in lista_produtos:
        if "produto_deletar" in st.session_state and st.session_state.produto_deletar == produto['id']:
            st.markdown('<div class="form-overlay-box" style="border-color:#ff3b3b;">', unsafe_allow_html=True)
            st.markdown(f"#### ⚠️ Confirmar exclusão do patrimônio?")
            st.write(f"Ativo selecionado: **{produto['nome']}**")
            
            if not eh_admin:
                st.warning("🔒 Operação bloqueada.")
            else:
                b1, b2 = st.columns(2)
                with b1:
                    if st.button("Sim, remover", key=f"real_del_{produto['id']}", type="primary", use_container_width=True):
                        try:
                            res = requests.delete(f"{API_URL}/{produto['id']}")
                            if res.status_code == 200:
                                st.toast("🗑️ Ativo removido!")
                                del st.session_state.produto_deletar
                                st.rerun()
                        except Exception: st.error("Erro.")
                with b2:
                    if st.button("Cancelar", key=f"cancel_del_{produto['id']}", use_container_width=True):
                        del st.session_state.produto_deletar
                        st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        if "produto_editar" in st.session_state and st.session_state.produto_editar == produto['id']:
            st.markdown('<div class="form-overlay-box">', unsafe_allow_html=True)
            st.markdown(f"#### ⚙️ Modificar Ativo Patrimonial (ID: {produto['id']})")
            
            if not eh_admin:
                st.warning("🔒 Operação bloqueada.")
            else:
                alt_nome = st.text_input("NOME", value=produto['nome'], key=f"form_n_{produto['id']}")
                alt_cat = st.text_input("CATEGORIA", value=produto['categoria'], key=f"form_c_{produto['id']}")
                alt_preco = st.number_input("VALOR (R$)", value=float(produto['preco']), key=f"form_p_{produto['id']}")
                alt_qtd = st.number_input("ESTOQUE", value=int(produto['quantidade']), key=f"form_q_{produto['id']}")
                alt_img = st.text_input("URL FOTO", value=produto['imagem_url'], key=f"form_i_{produto['id']}")
                
                bs, bc = st.columns(2)
                with bs:
                    if st.button("Gravar", key=f"form_save_{produto['id']}", type="primary", use_container_width=True):
                        payload = {"nome": alt_nome, "categoria": alt_cat, "preco": float(alt_preco), "quantidade": int(alt_qtd), "imagem_url": alt_img}
                        try:
                            res = requests.put(f"{API_URL}/{produto['id']}", json=payload)
                            if res.status_code == 200:
                                st.toast("💾 Alterações salvas!")
                                del st.session_state.produto_editar
                                st.rerun()
                        except Exception: st.error("Erro.")
                with bc:
                    if st.button("Descartar", key=f"form_canc_{produto['id']}", use_container_width=True):
                        del st.session_state.produto_editar
                        st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)