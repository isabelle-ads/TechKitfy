import streamlit as st

st.title("📊 Dashboard")

st.write("Bem-vindo ao painel administrativo da TechKitfy.")

st.write("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📦 Produtos")
    st.metric(label="Total", value="120")

with col2:
    st.success("👥 Clientes")
    st.metric(label="Total", value="85")

with col3:
    st.warning("🛒 Pedidos")
    st.metric(label="Total", value="43")

st.write("---")

st.subheader("📈 Atividades Recentes")

st.dataframe([
    {
        "Usuário": "Carlos",
        "Ação": "Comprou Notebook",
        "Status": "Concluído"
    },
    {
        "Usuário": "Ana",
        "Ação": "Cadastro realizado",
        "Status": "Novo"
    },
    {
        "Usuário": "Lucas",
        "Ação": "Pedido cancelado",
        "Status": "Pendente"
    }
])