from flask import Flask
from app.config import Config
from app.database import db
from flask_migrate import Migrate  # Importa o Flask-Migrate
from app.routes import main


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)  # Inicializa o Flask-Migrate
app.register_blueprint(main)

with app.app_context():
    db.create_all()
