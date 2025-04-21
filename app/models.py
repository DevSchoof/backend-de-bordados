from app.database import db

class Produto(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    alt = db.Column(db.String(200), nullable=False)
    url_imagem = db.Column(db.String(200), nullable=False)
 