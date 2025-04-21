from flask import Flask
from app.config import Config
from app.database import db
from app.routes import main


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(main)

with app.app_context():
    db.create_all()
    