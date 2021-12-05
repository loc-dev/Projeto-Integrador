# 03 - Criando o Blueprint de Idioma

import functools

from flask import (
    Blueprint, render_template
)

# Criando o nome do Blueprint com 'lang'
bp = Blueprint('lang', __name__)

# Primeira visualização com a função 'portuguese'
@bp.route('/')
def portuguese():

    return render_template('pt_br/landing_page.html')

# Visualização com a função 'spanish'
@bp.route('/es')
def spanish():

    return render_template('es_es/landing_page_es.html')