import os
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from fastapi.middleware.cors import CORSMiddleware

# 1. CONFIGURAÇÃO DO BANCO DE DADOS (SQLite)
DATABASE_URL = "sqlite:///./techkitfy.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelos do Banco de Dados (Tabelas)
class UsuarioModel(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)

class ProdutoModel(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    categoria = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)
    imagem_url = Column(String, nullable=True)

# Cria as tabelas no arquivo .db caso não existam
Base.metadata.create_all(bind=engine)

# Dependência para abrir e fechar a sessão do banco de dados de forma segura
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 2. INICIALIZAÇÃO DA API (FastAPI com correção de rota do Swagger)
app = FastAPI(
    title="TechKitfy API Core",
    description="Backend estruturado para controle patrimonial de ativos eletrônicos",
    version="1.0.0",
    servers=[
        {"url": "http://127.0.0.1:8000", "description": "Ambiente de Desenvolvimento Local"}
    ]
)

# Configuração de CORS para permitir que o Frontend se comunique com a API sem bloqueios
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Esquemas de Validação de Dados (Pydantic)
class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str

class UserLogin(BaseModel):
    email: EmailStr
    senha: str

class ProdutoCreate(BaseModel):
    nome: str
    categoria: str
    preco: float
    quantidade: int
    imagem_url: str = None

# --- ROTAS DE USUÁRIOS (Endpoints) ---
@app.post("/api/usuarios/registrar", status_code=status.HTTP_201_CREATED, tags=["Usuários"])
def registrar_usuario(user: UserCreate, db: Session = Depends(get_db)):
    existe = db.query(UsuarioModel).filter(UsuarioModel.email == user.email).first()
    if existe:
        raise HTTPException(status_code=400, detail="E-mail corporativo já cadastrado!")
    novo_usuario = UsuarioModel(nome=user.nome, email=user.email, senha=user.senha)
    db.add(novo_usuario)
    db.commit()
    return {"mensagem": "Usuário registrado com sucesso!"}

@app.post("/api/usuarios/login", tags=["Usuários"])
def login_usuario(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(UsuarioModel).filter(UsuarioModel.email == user.email, UsuarioModel.senha == user.senha).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="E-mail ou chave de acesso incorretos!")
    return {"status": "sucesso", "nome": db_user.nome, "email": db_user.email}

@app.get("/api/usuarios", tags=["Usuários"])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(UsuarioModel).all()

# ROTA ADICIONADA: Deleta permanentemente um colaborador do banco SQLite pelo ID
@app.delete("/api/usuarios/{user_id}", tags=["Usuários"])
def deletar_usuario(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UsuarioModel).filter(UsuarioModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Colaborador não localizado na infraestrutura")
    db.delete(user)
    db.commit()
    return {"mensagem": "Credenciais revogadas com sucesso!"}

# --- ROTAS DE PRODUTOS (Endpoints) ---
@app.post("/api/produtos", status_code=status.HTTP_201_CREATED, tags=["Produtos"])
def criar_produto(prod: ProdutoCreate, db: Session = Depends(get_db)):
    novo_prod = ProdutoModel(**prod.dict())
    db.add(novo_prod)
    db.commit()
    db.refresh(novo_prod)
    return novo_prod

@app.get("/api/produtos", tags=["Produtos"])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(ProdutoModel).all()

@app.delete("/api/produtos/{prod_id}", tags=["Produtos"])
def deletar_produto(prod_id: int, db: Session = Depends(get_db)):
    prod = db.query(ProdutoModel).filter(ProdutoModel.id == prod_id).first()
    if not prod:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    db.delete(prod)
    db.commit()
    return {"mensagem": "Ativo removido do patrimônio"}

@app.put("/api/produtos/{prod_id}", tags=["Produtos"])
def editar_produto(prod_id: int, prod: ProdutoCreate, db: Session = Depends(get_db)):
    db_prod = db.query(ProdutoModel).filter(ProdutoModel.id == prod_id).first()
    if not db_prod:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    db_prod.nome = prod.nome
    db_prod.categoria = prod.categoria
    db_prod.preco = prod.preco
    db_prod.quantidade = prod.quantidade
    db_prod.imagem_url = prod.imagem_url
    
    db.commit()
    db.refresh(db_prod)
    return db_prod