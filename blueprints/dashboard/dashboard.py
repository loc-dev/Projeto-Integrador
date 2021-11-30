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

# A função 'unico_refugiado', possibilita selecionar somente o refugiado de um determinado id, 
# para utilizar nas outras funções em que a visualização permitindo a alteração de dados e exclusão de conta
def unico_refugiado(id):
    refugee = get_db().execute(
        "SELECT * FROM refugiado WHERE id = ?",
        (id,)
    ).fetchone()

    print(refugee)
    return refugee

# Visualização em português sobre a página Dashboard Perfil para o usuário Refugiado, com a função 'pt_edit_refugiado' - Permitindo a alteração de dados
@bp.route('/dashboard/refugiado/perfil/<int:id>', methods=('GET', 'POST'))
@pt_login_required_refugiado
def pt_edit_refugiado(id):
    refugee = unico_refugiado(id)

    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        nacionalidade = request.form['nacionalidade']
        email = request.form['email']
        error = None

        if  not nome and not email:
            error = 'Por favor, os campos com ( * ) são obrigatórios!'
        elif not nome:
            error = 'Por favor, o Nome é obrigatório.'
        elif not email:
            error = 'Por favor, o E-mail é obrigatório.'
        
        
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE refugiado SET nome = ?, sobrenome = ?, nacionalidade = ?, email = ?"
                " WHERE id = ?",
                (nome, sobrenome, nacionalidade, email, id)
            )
            db.commit()
            return redirect(url_for('dashboard.pt_index_refugiado'))

    return render_template('pt_br/dashboard/pt_perfil_refugiado_page.html', refugee=refugee)

# Essa função 'pt_delete_refugiado' estará em funcionamento na página Dashboard Perfil para o usuário Refugiado - Permitindo a exclusão da conta
@bp.route('/dashboard/refugiado/perfil/<int:id>/excluir', methods=('GET', 'POST'))
@pt_login_required_refugiado
def pt_delete_refugiado(id):
    unico_refugiado(id)

    db = get_db()
    db.execute('DELETE FROM refugiado WHERE id = ?', (id,))
    db.commit()

    return redirect(url_for('auth.pt_login_refugiado'))

# Visualização em espanhol sobre a página Dashboard Perfil para o usuário Refugiado, com a função 'es_edit_refugiado' - Permitindo a alteração de dados
@bp.route('/dashboard/refugiado/perfil/<int:id>/es', methods=('GET', 'POST'))
@es_login_required_refugiado
def es_edit_refugiado(id):
    refugee = unico_refugiado(id)

    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        nacionalidade = request.form['nacionalidade']
        email = request.form['email']
        error = None

        if not nome and not email:
            error = '¡Por favor, los campos con (*) son obligatorios!'
        elif not nome:
            error = '¡Por favor, se requiere nombre!'
        elif not email:
            error = '¡Por favor, se require correo electrónico!'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE refugiado SET nome = ?, sobrenome = ?. nacionalidade = ?, email = ?"
                " WHERE id = ?",
                (nome, sobrenome, nacionalidade, email, id)
            )
            db.commit()
            return redirect(url_for('dashboard.es_index_refugiado'))

    return render_template('es_es/dashboard/es_perfil_refugiado_page.html', refugee=refugee)

# Essa função 'es_delete_refugiado' estará em funcionamento na página Dashboard Perfil para o usuário Refugiado - Permitindo a exclusão da conta
@bp.route('/dashboard/refugiado/perfil/<int:id>/eliminar/es', methods=('GET', 'POST'))
@es_login_required_refugiado
def es_delete_refugiado(id):
    unico_refugiado(id)

    db = get_db()
    db.execute('DELETE FROM refugiado WHERE id = ?', (id,))
    db.commit()

    return redirect(url_for('auth.es_login_refugiado'))
