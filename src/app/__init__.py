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

    from src.models import User, Motorista, Viagens, Depoimentos  # noqa: F401
    from src.app.routes.main_route import main

    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
