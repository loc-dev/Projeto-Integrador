# 06 - Criando o Blueprint de Dashboard (Refugiado e Voluntário em ambas versões português e espanhol)

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

# Importando a Função para exigir autenticação nas páginas internas do Dashboard para Refugiado em versão português
from blueprints.auth.auth import pt_login_required_refugiado

from imu.db import get_db

bp = Blueprint('dashboard', __name__)

# Visualização em português sobre a página Dashboard para o usuário Refugiado, com a função 'pt_index_refugiado'
@bp.route('/dashboard')
@pt_login_required_refugiado
def pt_index_refugiado():

    return render_template('pt_br/dashboard/pt_db_refugiado_page.html')
