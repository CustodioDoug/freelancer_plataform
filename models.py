from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    profissao = db.Column(db.String(100))
    valor = db.Column(db.Float)
    descricao = db.Column(db.Text)
