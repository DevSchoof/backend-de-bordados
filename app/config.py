import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', default='my_secret_key') 
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///meu_banco.db') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
