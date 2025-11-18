from datetime import datetime
from src.app import db

class Viagens(db.Model):
    __tablename__ = "viagens"

    id = db.Column(db.Integer, primary_key=True)

    client_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    motorista_id = db.Column(db.Integer, db.ForeignKey("motoristas.id"), nullable=False)

    tipo = db.Column(db.Integer, nullable=False)

    agendado_em = db.Column(db.DateTime, default=datetime.utcnow)
    data_ida = db.Column(db.Date, nullable=False)
    data_volta = db.Column(db.Date, nullable=False)

    local_embarque = db.Column(db.String(255), nullable=False)
    local_desembarque = db.Column(db.String(255), nullable=False)

    qntd_pessoas = db.Column(db.Integer, nullable=False)
    nomes = db.Column(db.JSON, default=list)

    depoimentos = db.relationship("Depoimentos", backref="viagem", lazy=True)