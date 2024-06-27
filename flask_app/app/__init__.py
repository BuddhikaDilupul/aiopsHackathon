from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config.config import Config  # Make sure to import from the correct location

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(Config)  # Use the Config class directly
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from app.controllers.count_controller import count_bp
    
    app.register_blueprint(count_bp)
    with app.app_context():
        db.create_all()

    return app
