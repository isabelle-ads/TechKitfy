import streamlit as st

st.title("🛒 Produtos")

requests.get("http://localhost:8000/produtos")