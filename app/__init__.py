from flask import Flask
from .config import Config
from .database import db
from .routes import main_routes

def create_app():
    
    app = Flask(__name__)
    app.register_blueprint(main_routes)
    app.config.from_object(Config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app