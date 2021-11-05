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
