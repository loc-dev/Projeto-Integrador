# 04 - Criando o Blueprint de Conteúdos (Home, Sobre nós, Workshops, Projetos)

import functools

from flask import (
    Blueprint, render_template
)

# Criando o nome do Blueprint com 'content'
bp = Blueprint('content', __name__)

# Visualização em português sobre a página Home, com a função 'pt_home'
@bp.route('/home')
def pt_home():

    return render_template('pt_br/home/home_page.html')

# Visualização em espanhol sobre a página Home, com a função 'es_home'
@bp.route('/home/es')
def es_home():

    return render_template('es_es/home/home_page_es.html')

# Visualização em português sobre a página Sobre nós, com a função 'pt_sobre'
@bp.route('/sobre')
def pt_sobre():

    return render_template('pt_br/sobre/sobre_page.html')

# Visualização em espanhol sobre a página Sobre nós, com a função 'es_sobre'
@bp.route('/sobre/es')
def es_sobre():

    return render_template('es_es/sobre/sobre_page_es.html')

# Visualização em português sobre a página Cadastrar, com a função 'pt_cadastrar'
@bp.route('/cadastrar')
def pt_cadastrar():

    return render_template('pt_br/cadastrar/cadastrar_page.html')

# Visualização em espanhol sobre a página Cadastrar, com a função 'es_cadastrar'
@bp.route('/cadastrar/es')
def es_cadastrar():

    return render_template('es_es/cadastrar/cadastrar_page_es.html')

# Visualização em português sobre a página Login, com a função 'pt_login'
@bp.route('/login')
def pt_login():

    return render_template('pt_br/login/login_page.html')

# Visualização em espanhol sobre a página Login, com a função 'es_login'
@bp.route('/login/es')
def es_login():

    return render_template('es_es/login/login_page_es.html')