from typing import List
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['banco-digital-dio']

endereco_collection = db['endereco']
cliente_collection = db['cliente']
conta_collection = db['conta_bancaria']

sandy = {
    'id': 1,
    'nome': 'sandy',
    'cpf': '07043257623',
}

bob = {
    'id': 2,
    'nome': 'bob',
    'cpf': '30043247623',
}

conta1 = {
    'id': 1,
    'tipo': 'fisica',
    'agencia': 'norte',
    'num': 213,
    'saldo': 1340.00,
    'id_cliente': 1,
}

conta2 = {
    'id': 2,
    'tipo': 'fisica',
    'agencia': 'sul',
    'num': 413,
    'saldo': 130.00,
    'id_cliente': 2,
}

cliente_collection.insert_many([sandy, bob])
conta_collection.insert_many([conta1, conta2])

users = cliente_collection.find({'nome': {'$in': ['bob', 'sandy']}})

for user in users:
    print(user['id'], user['nome'], user['cpf'])
