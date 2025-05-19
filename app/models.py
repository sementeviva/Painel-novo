from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(20))

class Conversa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.Text)
    resposta = db.Column(db.Text)
