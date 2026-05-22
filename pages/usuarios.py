import streamlit as st
import requests
from utils import carregar_design_premium

# 1. ACIONA O ENVELOPAMENTO VISUAL DO MENU LATERAL E TEMA ESCURO
carregar_design_premium()

# URL base da sua API FastAPI para usuários
API_URL = "http://127.0.0.1:8000/api/usuarios"

st.markdown('<div class="main-neon-title">👥 controle de acessos (iam)</div>', unsafe_allow_html=True)
st.markdown('<div class="main-sub-title">Painel executivo de auditoria de credenciais e privilégios integrados ao banco SQLite.</div>', unsafe_allow_html=True)

# 2. BARREIRA DE SEGURANÇA COMERCIAL
if "nivel_acesso" not in st.session_state or st.session_state.nivel_acesso != "admin":
    st.error("🔒 Área Confidencial. Apenas administradores do Core Team possuem permissão para auditar credenciais.")
else:
    # Estilização em CSS inline premium para manter a simetria com o catálogo
    st.markdown("""
        <style>
        .user-panel-box {
            background-color: #0b0f19;
            border: 1px solid rgba(0, 247, 255, 0.15);
            border-radius: 14px;
            padding: 22px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
            margin-top: 15px;
        }
        
        .user-row-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 14px 18px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            transition: all 0.2s ease;
        }
        .user-row-item:hover {
            background-color: rgba(0, 247, 255, 0.02);
        }
        .user-row-item:last-child {
            border-bottom: none;
        }
        
        .user-meta {
            text-align: left;
            flex-grow: 1;
        }
        .user-display-name {
            color: #ffffff;
            font-weight: 700;
            font-size: 1.05rem;
        }
        .user-display-email {
            color: #8c97a8;
            font-size: 0.82rem;
            font-family: monospace;
            margin-top: 2px;
        }
        
        .user-actions-block {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        /* Badges de Privilégio Estilo SaaS */
        .role-tag {
            font-family: 'Orbitron', sans-serif;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 5px 12px;
            border-radius: 20px;
            letter-spacing: 0.5px;
            display: inline-block;
            text-align: center;
            min-width: 100px;
        }
        .role-admin-core {
            background: rgba(0, 247, 255, 0.12);
            color: #00f7ff;
            border: 1px solid rgba(0, 247, 255, 0.3);
            box-shadow: 0 0 8px rgba(0, 247, 255, 0.15);
        }
        .role-colaborador-core {
            background: rgba(0, 255, 170, 0.08);
            color: #00ffaa;
            border: 1px solid rgba(0, 255, 170, 0.2);
        }
        
        /* Popups de confirmação abaixo da tabela */
        .form-overlay-box {
            background-color: #111726;
            border: 2px solid #ff3b3b;
            border-radius: 12px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0 0 20px rgba(255, 59, 59, 0.2);
        }
        </style>
    """, unsafe_allow_html=True)

    # 3. CONSULTA OS DADOS EM TEMPO REAL DIRETO DO BACKEND FASTAPI
    lista_usuarios = []
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            lista_usuarios = response.json()
    except Exception:
        st.error("❌ Falha crítica: O servidor Backend FastAPI está online?")

    # 4. FERRAMENTA DE FILTRO / PESQUISA OPERACIONAL
    pesquisa = st.text_input("🔍 FILTRAR COLABORADOR POR NOME OU E-MAIL", placeholder="Digite o termo de busca...")
    st.write("<br>", unsafe_allow_html=True)

    if not lista_usuarios:
        st.info("ℹ️ Nenhuma credencial localizada na infraestrutura SQLite local.")
    else:
        # Aplica o filtro de pesquisa dinamicamente na lista vinda da API
        usuarios_filtrados = [
            u for u in lista_usuarios 
            if pesquisa.lower() in u.get("nome", "").lower() or pesquisa.lower() in u.get("email", "").lower()
        ]
        
        st.markdown(f"##### Registros Auditados: `{len(usuarios_filtrados)}` de `{len(lista_usuarios)}` total")
        
        # Renderiza a tabela em um container premium integrado
        st.markdown('<div class="user-panel-box">', unsafe_allow_html=True)
        
        for usuario in usuarios_filtrados:
            u_id = usuario.get("id")
            u_nome = usuario.get("nome", "Identidade Não Informada")
            u_email = usuario.get("email", "N/A")
            
            # Validação lógica do badge com base no e-mail real do banco
            if "admin" in u_email.lower():
                badge_style = "role-tag role-admin-core"
                badge_label = "🔒 Admin Core"
                pode_deletar = False  # Proteção para o admin não se autodeletar
            else:
                badge_style = "role-tag role-colaborador-core"
                badge_label = "👤 Colaborador"
                pode_deletar = True
                
            # Cria colunas nativas internas na linha para acoplar o botão do Streamlit perfeitamente alinhado
            col_dados, col_botoes = st.columns([4, 2])
            
            with col_dados:
                st.markdown(f"""
                    <div class="user-row-item" style="border-bottom: none; padding: 0;">
                        <div class="user-meta">
                            <div class="user-display-name">👤 {u_nome}</div>
                            <div class="user-display-email">{u_email}</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
            with col_botoes:
                # Alinha o badge HTML e o botão de lixeira lado a lado na direita
                c_badge, c_lixo = st.columns([2, 1])
                with c_badge:
                    st.markdown(f'<span class="{badge_style}" style="margin-top: 5px;">{badge_label}</span>', unsafe_allow_html=True)
                with c_lixo:
                    if pode_deletar:
                        if st.button("🗑️", key=f"del_user_{u_id}", use_container_width=True):
                            st.session_state.usuario_deletar_id = u_id
                            st.session_state.usuario_deletar_nome = u_nome
                            st.rerun()
                    else:
                        st.write("") # Fica em branco para admins (bloqueado deletar)
                        
            st.markdown('<hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.05); margin: 5px 0;">', unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

        # 5. FORMULÁRIO DE CONFIRMAÇÃO DE EXCLUSÃO (Aparece embaixo se clicado)
        if "usuario_deletar_id" in st.session_state:
            st.markdown('<div class="form-overlay-box">', unsafe_allow_html=True)
            st.markdown(f"#### ⚠️ Revogar Acesso do Sistema?")
            st.write(f"Tem certeza que deseja apagar permanentemente o colaborador **{st.session_state.usuario_deletar_nome}** do banco SQLite?")
            
            b_sim, b_nao = st.columns(2)
            with b_sim:
                if st.button("Sim, Deletar Conta", type="primary", use_container_width=True):
                    try:
                        res = requests.delete(f"{API_URL}/{st.session_state.usuario_deletar_id}")
                        if res.status_code == 200:
                            st.toast("🗑️ Credenciais revogadas com sucesso!")
                            del st.session_state.usuario_deletar_id
                            del st.session_state.usuario_deletar_nome
                            st.rerun()
                        else:
                            st.error("Erro ao deletar usuário no backend.")
                    except Exception:
                        st.error("Erro de comunicação com o servidor.")
            with b_nao:
                if st.button("Cancelar", use_container_width=True):
                    del st.session_state.usuario_deletar_id
                    del st.session_state.usuario_deletar_nome
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)