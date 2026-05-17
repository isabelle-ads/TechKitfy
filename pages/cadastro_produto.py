import streamlit as st

st.title("📦 Cadastro de Equipamentos / Produtos")

# Regra de Segurança: Se não for admin, não vê o formulário (RNF01) 
if "nivel_acesso" not in st.session_state or st.session_state.nivel_acesso != "admin":
    st.error("Acesso restrito! Apenas administradores do sistema podem cadastrar produtos.")
else:
    st.write("Preencha os dados do equipamento obtidos pela Engenharia de Requisitos[cite: 5, 7]:")
    
    with st.form("cadastro_ti"):
        nome = st.text_input("Nome do Equipamento")
        patrimonio = st.text_input("Número de Patrimônio")
        marca = st.text_input("Marca")
        modelo = st.text_input("Modelo")
        setor = st.selectbox("Setor Responsável", ["Estoque Central", "TI Interno", "Vendas"])
        estado = st.selectbox("Estado do Equipamento [cite: 10]", ["Disponível", "Em manutenção", "Em uso", "Descartado"])
        
        if st.form_submit_button("Salvar Registro"):
            st.success(f"Equipamento {nome} (Patrimônio: {patrimonio}) guardado com sucesso!")