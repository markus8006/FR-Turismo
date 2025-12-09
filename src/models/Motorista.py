from datetime import datetime

from src.app import db


class Motorista(db.Model):
    __tablename__ = "motoristas"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    CPF = db.Column(db.String(14), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    telefone = db.Column(db.String(20), nullable=False)
    status = db.Column(db.Boolean, default=True)

    viagens = db.relationship("Viagens", backref="motorista", lazy=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return f"<Motorista {self.email}>"
