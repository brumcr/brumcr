#models.py
from projetofacu import db
from datetime import datetime

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    senha = db.Column(db.String, nullable=False)
    foto_perfil = db.Column(db.String, default='default.jpg')
    posts = db.relationship('Post', backref='autor', lazy=True)
    cursos = db.Column(db.String, nullable=False, default='Não informado')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    corpo = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

class Escola(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    logradouro = db.Column(db.String, nullable=False)
    endereco = db.Column(db.String, nullable=False)
    cep = db.Column(db.Integer, nullable=False)
    ddd = db.Column(db.Integer, nullable=False)
    telefone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    sobrenome = db.Column(db.String, nullable=False)
    cpf = db.Column(db.Integer, nullable=False, unique=True)
    ddd = db.Column(db.Integer, nullable=False)
    telefone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)

class Disciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    carga = db.Column(db.Integer, nullable=False)
    cpf = db.Column(db.Integer, nullable=False, unique=True)

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    carga = db.Column(db.Integer, nullable=False)

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    dia = db.Column(db.String, nullable=False)
    disciplina = db.Column(db.String, nullable=False)
    professor = db.Column(db.String, nullable=False)