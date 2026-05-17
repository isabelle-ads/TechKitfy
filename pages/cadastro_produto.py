import streamlit as st

st.title("📦 Cadastro de Equipamentos / Produtos")

# 🔒 TRAVA DE SEGURANÇA (RNF01): Impede acessos não autorizados
if "nivel_acesso" not in st.session_state or st.session_state.nivel_acesso != "admin":
    st.error("❌ Acesso restrito! Apenas administradores do sistema podem cadastrar novos equipamentos.")
else:
    st.write("Insira as informações do eletroeletrónico para o inventário de TI:")
    
    with st.form("form_cadastro_ti"):
        nome = st.text_input("Nome do Equipamento")
        patrimonio = st.text_input("Número de Patrimônio")
        marca = st.text_input("Marca")
        modelo = st.text_input("Modelo")
        setor = st.selectbox("Setor Responsável", ["Estoque Central", "TI Interno", "Suporte Tecnológico", "Financeiro"])
        estado = st.selectbox("Estado do Equipamento", ["Disponível", "Em manutenção", "Em uso", "Descartado"])
        
        if st.form_submit_button("Salvar Registro"):
            # Aqui no futuro entrará a conexão com a API da Vic
            st.success(f"Sucesso! {nome} (Patrimônio: {patrimonio}) foi registrado no sistema.")