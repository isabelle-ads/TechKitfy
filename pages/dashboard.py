import streamlit as st

st.title("📊 Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Produtos", "120")
col2.metric("Clientes", "85")
col3.metric("Pedidos", "43")

st.write("---")

st.subheader("Resumo do Sistema")

st.write("""
Sistema desenvolvido para a disciplina APS.
""")