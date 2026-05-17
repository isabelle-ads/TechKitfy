import streamlit as st

# SESSION STATE

if "usuarios" not in st.session_state:

    st.session_state.usuarios = [

        {
            "nome": "Administrador",
            "email": "admin@gmail.com",
            "tipo": "Admin"
        },

        {
            "nome": "João",
            "email": "joao@gmail.com",
            "tipo": "Cliente"
        }

    ]

# TÍTULO

st.title("👥 Usuários")

st.write("Gerenciamento de usuários do sistema.")

st.write("---")

# FORMULÁRIO

st.subheader("➕ Novo Usuário")

col1, col2 = st.columns(2)

with col1:

    nome = st.text_input("Nome")

    email = st.text_input("Email")

with col2:

    tipo = st.selectbox(
        "Tipo de Usuário",
        [
            "Admin",
            "Cliente"
        ]
    )

# BOTÃO

if st.button("Cadastrar Usuário"):

    novo_usuario = {

        "nome": nome,
        "email": email,
        "tipo": tipo
    }

    st.session_state.usuarios.append(
        novo_usuario
    )

    st.success("✅ Usuário cadastrado!")

st.write("---")

# PESQUISA

pesquisa = st.text_input(
    "🔍 Pesquisar usuário"
)

st.write("---")

# LISTAGEM

st.subheader("📋 Lista de Usuários")

for i, usuario in enumerate(
    st.session_state.usuarios
):

    if pesquisa.lower() not in usuario["nome"].lower():

        continue

    with st.container(border=True):

        col1, col2, col3, col4 = st.columns(
            [3, 3, 2, 1]
        )

        col1.write(f"👤 {usuario['nome']}")

        col2.write(f"📧 {usuario['email']}")

        col3.write(f"🔑 {usuario['tipo']}")

        if col4.button(
            "🗑️",
            key=i
        ):

            st.session_state.usuarios.pop(i)

            st.rerun()