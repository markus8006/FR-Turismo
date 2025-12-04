from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.app.config import Config
from src.app.routes.main_route import main

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
        print(os.path.join(app.root_path, app.template_folder))
        db.create_all()
        app.register_blueprint(main)

    
    return app