# utils.py
import streamlit as st

def carregar_design_premium():
    """ Injeta o CSS global da TechKitfy para unificar o menu lateral e o tema escuro """
    st.markdown("""
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Orbitron:wght@400..900&display=swap" rel="stylesheet">
        
        <style>
        /* Fundo global e fontes */
        html, body, [data-testid="stAppViewContainer"] {
            font-family: "Montserrat", sans-serif;
            background-color: #0d1117 !important;
        }
        
        /* ----------------------------------------------------
           MENU LATERAL SUPREMO (SIDEBAR) 
        ---------------------------------------------------- */
        /* Fundo escuro e borda ciano fina e elegante */
        [data-testid="stSidebar"] {
            background-color: #0b0f19 !important;
            border-right: 2px solid rgba(0, 247, 255, 0.15) !important;
        }
        
        /* Ajuste do container de navegação para dar mais espaçamento (Aumenta o visual) */
        [data-testid="stSidebarNav"] {
            padding-top: 20px !important;
        }
        
        /* Texto dos links brancos, maiores e mais espaçados */
        [data-testid="stSidebarNav"] ul li a span {
            color: #e2e8f0 !important;
            font-family: "Montserrat", sans-serif;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        /* Efeito de Hover (passar o mouse) - Ilumina em ciano e dá profundidade */
        [data-testid="stSidebarNav"] ul li a:hover {
            background-color: rgba(0, 247, 255, 0.08) !important;
            border-radius: 8px;
            transform: translateX(3px);
        }
        [data-testid="stSidebarNav"] ul li a:hover span {
            color: #00f7ff !important;
            text-shadow: 0 0 10px rgba(0, 247, 255, 0.5);
        }
        
        /* Página Ativa selecionada: Fundo gradiente com traço ciano aceso */
        [data-testid="stSidebarNav"] ul li [data-testid="stSidebarNavLinkActive"] {
            background: linear-gradient(90deg, rgba(0, 247, 255, 0.15) 0%, rgba(0, 0, 0, 0) 100%) !important;
            border-left: 4px solid #00f7ff !important;
            border-radius: 0 8px 8px 0;
            box-shadow: inset 5px 0 15px rgba(0, 247, 255, 0.05);
        }
        [data-testid="stSidebarNav"] ul li [data-testid="stSidebarNavLinkActive"] span {
            color: #00f7ff !important;
            font-weight: 800 !important;
            text-shadow: 0 0 12px rgba(0, 247, 255, 0.4);
        }
        
        /* Seta de colapso da sidebar */
        [data-testid="stSidebarCollapseButton"] {
            color: #00f7ff !important;
        }
        </style>
    """, unsafe_allow_html=True)