from datetime import datetime

from src.app import db


class Depoimentos(db.Model):
    __tablename__ = "depoimentos"

    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=5)

    client_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    viagem_id = db.Column(db.Integer, db.ForeignKey("viagens.id"))

    conteudo = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return f"<Depoimento {self.author_name} ({self.rating} estrelas)>"
