# 🖥️ TechKitfy

<div align="center">

Sistema web para gerenciamento de uma loja de tecnologia, desenvolvido para a disciplina de Análise e Projeto de Sistemas (APS).

Frontend desenvolvido com Python + Streamlit.

</div>

---

# 👥 Desenvolvido por:

Isabelle Fernandes Juarez | 
Maria Vitória Alcânta da Silva | 
Lucas Gabriel da Silva Silveira 

---

# 📌 Sobre o Projeto

O **TechKitfy** é uma aplicação web desenvolvida com foco em gerenciamento de produtos, usuários e operações administrativas de uma loja de tecnologia.

O projeto foi construído utilizando arquitetura modular, interface responsiva e integração preparada para APIs REST com FastAPI.

---

# 🚀 Funcionalidades

## 🔐 Autenticação
- Login de usuários
- Validação de credenciais
- Controle de navegação

---

## 📊 Dashboard
- Métricas administrativas
- Visualização de dados
- Cards informativos
- Interface moderna

---

## 🛒 Produtos
- Cadastro de produtos
- Edição de produtos
- Exclusão de produtos
- Pesquisa dinâmica
- Filtro por categoria
- Upload de imagens
- Cards visuais

---

## 👤 Usuários
- Cadastro de usuários
- Gerenciamento administrativo
- Listagem de usuários
- Exclusão de usuários

---

# 🧱 Arquitetura do Projeto

```bash
TechKitfy/
│
├── .github/
│   └── workflows/
│       └── main.yml
│
├── .streamlit/
│   └── config.toml
│
├── pages/
│   ├── 1_Login.py
│   ├── 2_Produtos.py
│   ├── 3_Dashboard.py
│   └── 5_Usuarios.py
│
├── services/
│
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# 🛠️ Tecnologias Utilizadas

<div align="center">

| Tecnologia | Descrição |
|---|---|
| Python | Linguagem principal |
| Streamlit | Frontend Web |
| Pandas | Manipulação de dados |
| Docker | Containerização |
| GitHub Actions | CI/CD |
| Git/GitHub | Versionamento |

</div>

---

# ▶️ Executando o Projeto

## 1️⃣ Clonar repositório

```bash
git clone https://github.com/isabelle-ads/TechKitfy.git
```

---

## 2️⃣ Acessar pasta do projeto

```bash
cd TechKitfy
```

---

## 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Executar aplicação

```bash
streamlit run app.py
```

---

# 🐳 Executando com Docker

## Build da imagem

```bash
docker build -t techkitfy .
```

---

## Rodar container

```bash
docker run -p 8501:8501 techkitfy
```

---

# 🔄 Integração Contínua

O projeto utiliza GitHub Actions para automação de integração contínua (CI/CD), realizando:

- Instalação automática das dependências
- Verificação de build
- Execução automatizada em pushes para o repositório

---

# 🎨 Interface

O sistema foi desenvolvido com foco em:

- UI/UX moderna
- Responsividade
- Navegação intuitiva
- Organização visual
- Experiência do usuário

---

# 📚 Objetivos Acadêmicos

Este projeto foi desenvolvido com fins acadêmicos para prática de:

- Desenvolvimento Frontend
- Arquitetura de Software
- CRUD
- Docker
- GitHub Actions
- Integração Full Stack
- Boas práticas de desenvolvimento

---

# 👨‍💻 Equipe 

<div align="center">

| Nome | Função |
|---|---|
| Isabelle Fernandes | Frontend / UI & UX |
| Maria Vitória | Backend |
| Lucas Gabriel | Banco de Dados |

</div>

---

# 📄 Licença

Projeto acadêmico desenvolvido para fins educacionais.

---

<div align="center">

### 🚀 TechKitfy

Sistema de Loja de Tecnologia

</div>