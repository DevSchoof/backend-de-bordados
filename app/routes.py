from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.database import db
from app.models import Produto


main  = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/produto', methods=['GET', 'POST'])
def produto():
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        alt = request.form.get('alt')
        url_imagem = request.form.get('url_imagem')
        print(nome, descricao, alt, url_imagem)
        

        if not nome or not descricao or not alt or not url_imagem:
            flash('Nome, descrição, alt e URL da imagem são obrigatórios!')
            return redirect(url_for('main.produto'))
        else:
            novo_produto = Produto(nome=nome, 
                                    descricao=descricao, 
                                    alt=alt, 
                                    url_imagem=url_imagem)
            db.session.add(novo_produto)
            db.session.commit()
            flash('Produto adicionado com sucesso!')
            return redirect(url_for('main.produto'))
      
       
    
    return render_template('produto.html')
