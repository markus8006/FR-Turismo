from datetime import datetime
from src.app import db

class Depoimentos(db.Model):
    __tablename__ = "depoimentos"

    id = db.Column(db.Integer, primary_key=True)

    client_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    viagem_id = db.Column(db.Integer, db.ForeignKey("viagens.id"))

    conteudo = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)