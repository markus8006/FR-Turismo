from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.app.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from src.models import (
        Users,
        Motorista,
        Viagens,
        Depoimentos
    )
    with app.app_context():
        db.create_all()

    return app