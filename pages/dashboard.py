import streamlit as st

st.title("📊 Dashboard Administrativo de TI")

# 🔒 TRAVA DE SEGURANÇA: Bloqueia dados corporativos confidenciais
if "nivel_acesso" not in st.session_state or st.session_state.nivel_acesso != "admin":
    st.error("❌ Acesso bloqueado! Esta tela contém dados confidenciais do estoque da empresa.")
else:
    st.subheader("Indicadores e métricas de controle patrimonial")
    
    # Exibição em colunas (Métricas rápidas)
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Equipamentos", "154 itens")
    col2.metric("Disponíveis / Em Uso", "142 itens")
    col3.metric("Em Manutenção", "12 itens", delta="-2 resolvidos", delta_color="inverse")
    
    st.markdown("---")
    st.write("### 📈 Quantidade de Equipamentos alocados por Setor")
    
    # Gráfico de barras nativo do Streamlit (Atende ao RF09)
    dados_grafico = {"TI Interno": 45, "Suporte": 35, "Financeiro": 20, "RH": 15, "Estoque": 39}
    st.bar_chart(dados_grafico)