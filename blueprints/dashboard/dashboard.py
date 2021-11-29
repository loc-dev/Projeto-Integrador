# 06 - Criando o Blueprint de Dashboard (Refugiado e Voluntário em ambas versões português e espanhol)

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

# Importando a Função para exigir autenticação nas páginas internas do Dashboard para Refugiado em ambas versões de idioma
from blueprints.auth.auth import pt_login_required_refugiado
from blueprints.auth.auth import es_login_required_refugiado

# Importando a Função para exigir autenticação nas páginas internas do Dashboard para Voluntário em ambas versões de idioma
from blueprints.auth.auth import pt_login_required_voluntario
from blueprints.auth.auth import es_login_required_voluntario


from imu.db import get_db

bp = Blueprint('dashboard', __name__)

# Visualização em português sobre a página Dashboard para o usuário Refugiado, com a função 'pt_index_refugiado'
@bp.route('/dashboard/refugiado')
@pt_login_required_refugiado
def pt_index_refugiado():

    return render_template('pt_br/dashboard/pt_db_refugiado_page.html')

# Visualização em espanhol sobre a página Dashboard para o usuário Refugiado, com a função 'es_index_refugiado'
@bp.route('/dashboard/refugiado/es')
@es_login_required_refugiado
def es_index_refugiado():

    return render_template('es_es/dashboard/es_db_refugiado_page.html')

# Visualização em português sobre a página Dashboard para o usuário Voluntário, com a função 'pt_index_voluntario'
@bp.route('/dashboard/voluntario')
@pt_login_required_voluntario
def pt_index_voluntario():

    return render_template('pt_br/dashboard/pt_db_voluntario_page.html')

# Visualização em espanhol sobre a página Dashboard para o usuário Voluntário, com a função 'es_index_voluntario'
@bp.route('/dashboard/voluntario/es')
@es_login_required_voluntario
def es_index_voluntario():

    return render_template('es_es/dashboard/es_db_voluntario_page.html')
