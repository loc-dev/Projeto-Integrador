# 04 - Criando o Blueprint de Conteúdos (Home, Sobre nós, Workshops, Projetos)

import functools

from flask import (
    Blueprint, render_template
)

# Criando o nome do Blueprint com 'content'
bp = Blueprint('content', __name__)

# Visualização em português sobre a página Home, com a função 'pt_home'
@bp.route('/index')
def pt_home():

    return render_template('pt_br/home/home.html')
