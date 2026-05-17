import streamlit as st

st.title("📊 Dashboard Administrativo de TI")

if "nivel_acesso" not in st.session_state or st.session_state.nivel_acesso != "admin":
    st.error("Acesso bloqueado! Esta tela contém dados confidenciais de estoque corporativo[cite: 11, 13].")
else:
    st.subheader("Informações resumidas dos equipamentos do sistema ")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total em Estoque", "154 itens")
    col2.metric("Em Uso", "89 itens")
    col3.metric("Manutenção [cite: 10]", "12 itens")
    
    st.markdown("---")
    st.write("### Equipamentos por Setor")
    dados_mockados = {"TI": 40, "RH": 12, "Suporte": 35, "Financeiro": 18}
    st.bar_chart(dados_mockados)