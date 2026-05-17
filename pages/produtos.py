import streamlit as st

def carregar_estilo_premium():
    
    st.markdown("""
        <link rel="precoportfólionnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Orbitron:wght@400..900&display=swap" rel="stylesheet">
        
        <style>
      
        html, body, [data-testid="stAppViewContainer"] {
            font-family: "Montserrat", sans-serif;
            background-color: #0f0f1e !important;
        }
        
        
        .neon-title {
            font-family: "Orbitron", sans-serif;
            color: #00f7ff;
            text-shadow: 0 0 15px rgba(0, 247, 255, 0.6);
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 5px;
        }
        
        .sub-neon {
            color: #8c97a8;
            font-size: 0.95rem;
            margin-bottom: 25px;
        }
        
        
        .tech-card {
            background: linear-gradient(135deg, #16162d 0%, #0f0f1e 100%);
            border: 1px solid rgba(0, 247, 255, 0.15);
            border-radius: 16px;
            padding: 20px;
            text-align: center;
            position: relative;
            overflow: hidden;
            transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }
        
        
        .tech-card:hover {
            transform: translateY(-8px);
            border-color: #00f7ff;
            box-shadow: 0 0 25px rgba(0, 247, 255, 0.35);
        }
        
        
        .tech-card::before {
            content: '';
            position: absolute;
            top: -50px;
            right: -50px;
            width: 100px;
            height: 100px;
            background: rgba(0, 247, 255, 0.03);
            border-radius: 50%;
            filter: blur(10px);
        }
        
        .product-image-container img {
            width: 100%;
            height: 160px;
            object-fit: cover;
            border-radius: 12px;
            filter: drop-shadow(0px 10px 15px rgba(0,0,0,0.5));
            transition: transform 0.5s ease;
        }
        
        .tech-card:hover .product-image-container img {
            transform: scale(1.05);
        }
        
        .prod-name {
            font-family: "Montserrat", sans-serif;
            font-weight: 700;
            font-size: 1.2rem;
            color: #ffffff;
            margin-top: 15px;
            min-height: 35px;
        }
        
        .prod-category {
            font-family: "Orbitron", sans-serif;
            font-size: 0.75rem;
            color: #00f7ff;
            background: rgba(0, 247, 255, 0.08);
            padding: 4px 12px;
            border-radius: 20px;
            display: inline-block;
            margin-bottom: 15px;
            border: 1px solid rgba(0, 247, 255, 0.2);
        }
        
        .prod-price-tag {
            font-family: "Orbitron", sans-serif;
            font-size: 1.5rem;
            font-weight: 800;
            color: #ffffff;
            text-shadow: 0 0 8px rgba(255, 255, 255, 0.2);
            margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)


carregar_estilo_premium()


st.markdown('<div class="neon-title">⚙️ TechKitfy Stock</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-neon">Catálogo | Encontre as melhores marcas para o seu dispositivo.</div>', unsafe_allow_html=True)


if "produtos" not in st.session_state:
    st.session_state.produtos = [
        {"nome": "MacBook Pro M3", "preco": 18499.00, "categoria": "Notebook", "imagem": "https://images.unsplash.com/photo-1517336714739-489689fd1ca8"},
        {"nome": "AirPods Max Neon", "preco": 5290.00, "categoria": "Headphone", "imagem": "https://images.unsplash.com/photo-1546435770-a3e426bf472b"},
        {"nome": "Monitor Vision Ultra", "preco": 3899.00, "categoria": "Monitor", "imagem": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf"}
    ]


cols = st.columns(3)

for i, produto in enumerate(st.session_state.produtos):
    col_idx = i % 3
    with cols[col_idx]:
       
        st.markdown(f"""
            <div class="tech-card">
                <div class="product-image-container">
                    <img src="{produto['imagem']}">
                </div>
                <div class="prod-name">{produto['nome']}</div>
                <div style="margin: 8px 0;"><span class="prod-category">{produto['categoria']}</span></div>
                <div class="prod-price-tag">R$ {produto['preco']:.2f}</div>
            </div>
        """, unsafe_allow_html=True)
        
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✏️ Editar", key=f"edit_{i}", use_container_width=True):
                st.session_state.produto_editar = i
                st.rerun()
        with c2:
            if st.button("🗑️ Apagar", key=f"del_{i}", use_container_width=True):
                st.session_state.produtos.pop(i)
                st.toast(f"🗑️ {produto['nome']} removido do sistema!")
                st.rerun()