from typing import List, Optional
from sqlalchemy import create_engine, String, select, Column, Integer, Float
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey

DeclarativeBase = declarative_base()

class Endereco(DeclarativeBase):
    __tablename__ = "endereco"
    id = Column(Integer, primary_key=True)
    logradouro = Column(String(45))
    numero = Column(Integer)
    cep = Column(String(8))
    cliente_id = Column(Integer, ForeignKey("cliente.id"))

class Cliente(DeclarativeBase):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(11))

class Conta(DeclarativeBase):
    __tablename__ = "conta_bancaria"
    id = Column(Integer, primary_key=True)
    tipo = Column(String(15))
    agencia = Column(String(20))  # Add the data type here
    num = Column(Integer)
    saldo = Column(Float)
    id_cliente = Column(Integer, ForeignKey("cliente.id"))

engine = create_engine("sqlite://", echo=True)

sandy = Cliente(
    id=1,
    nome='sandy',
    cpf='07043257623',
)

bob = Cliente(
    id=2,
    nome='bob',
    cpf='30043247623',
)

conta1 = Conta(
    id=1,
    tipo='fisica',
    agencia='norte',
    num=213,
    saldo=1340.00,
    id_cliente=1,
)

conta2 = Conta(
    id=2,
    tipo='fisica',
    agencia='sul',
    num=413,
    saldo=130.00,
    id_cliente=2,
)

DeclarativeBase.metadata.create_all(engine)

# Adding clients and committing the changes
with Session(engine) as session:
    session.add_all([bob, sandy, conta1, conta2])
    session.commit()

# Querying and printing users
with Session(engine) as session:
    stmt = select(Cliente).where(Cliente.nome.in_(["bob", "sandy"]))
    users = session.execute(stmt).scalars().all()

    for user in users:
        print(user.id, user.nome, user.cpf)
