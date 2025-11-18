from datetime import datetime
from src.app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    telefone = db.Column(db.String(20), nullable=False)
    CPF = db.Column(db.String(20), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Boolean, default=True)


    viagens = db.relationship("Viagens", backref="cliente", lazy=True)
    depoimentos = db.relationship("Depoimentos", backref="autor", lazy=True)