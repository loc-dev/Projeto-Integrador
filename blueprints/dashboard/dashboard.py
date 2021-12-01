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
                "UPDATE refugiado SET nome = ?, sobrenome = ?, nacionalidade = ?, email = ?"
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

# Visualização em português da função 'pt_workshop_refugiado' será apresentado as publicações que foram recém-criadas, as mais recentes estão em destaque primeiro
@bp.route('/dashboard/refugiado/workshop')
@pt_login_required_refugiado
def pt_workshop_refugiado():
    db = get_db()
    publicacoes = db.execute(
        "SELECT p.id, title, body, created, author_id, nome"
        " FROM workshop p JOIN voluntario v ON p.author_id = v.id"
        " ORDER BY created DESC"
    ).fetchall()

    return render_template('pt_br/dashboard/pt_workshop_refugiado_page.html', publicacoes=publicacoes)


# A função 'unico_voluntario', possibilita selecionar somente o refugiado de um determinado id,
# para utilizar nas outras funções em que a visualização permitindo a alteração de dados e exclusão de conta
def unico_voluntario(id):
    volunteer = get_db().execute(
        "SELECT * FROM voluntario WHERE id = ?",
        (id,)
    ).fetchone()

    return volunteer

# Visualização em português sobre a página Dashboard Perfil para o usuário Voluntário, com a função 'pt_edit_voluntario' - Permitindo a alteração de dados
@bp.route('/dashboard/voluntario/perfil/<int:id>', methods=('GET', 'POST'))
@pt_login_required_voluntario
def pt_edit_voluntario(id):
    volunteer = unico_voluntario(id)

    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
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
                "UPDATE voluntario SET nome = ?, sobrenome = ?, email = ?"
                " WHERE id = ?",
                (nome, sobrenome, email, id)
            )
            db.commit()
            return redirect(url_for('dashboard.pt_index_voluntario'))

    return render_template('pt_br/dashboard/pt_perfil_voluntario_page.html', volunteer=volunteer)

# Essa função 'pt_delete_voluntario' estará em funcionamento na página Dashboard Perfil para o usuário Voluntário - Permitindo a exclusão da conta
@bp.route('/dashboard/voluntario/perfil/<int:id>/excluir', methods=('GET', 'POST'))
@pt_login_required_voluntario
def pt_delete_voluntario(id):
    unico_voluntario(id)

    db = get_db()
    db.execute('DELETE FROM voluntario WHERE id = ?', (id,))
    db.commit()

    return redirect(url_for('auth.pt_login_voluntario'))

# Visualização em espanhol sobre a página Dashboard Perfil para o usuário Voluntário, com a função 'es_edit_voluntario' - Permitindo a alteração de dados
@bp.route('/dashboard/voluntario/perfil/<int:id>/es', methods=('GET', 'POST'))
@es_login_required_voluntario
def es_edit_voluntario(id):
    volunteer = unico_voluntario(id)

    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
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
                "UPDATE voluntario SET nome = ?, sobrenome = ?, email = ?"
                " WHERE id = ?",
                (nome, sobrenome, email, id)
            )
            db.commit()
            return redirect(url_for('dashboard.es_index_voluntario'))

    return render_template('es_es/dashboard/es_perfil_voluntario_page.html', volunteer=volunteer)

# Essa função 'es_delete_voluntario' estará em funcionamento na página Dashboard Perfil para o usuário Voluntário - Permitindo a exclusão da conta
@bp.route('/dashboard/voluntario/perfil/<int:id>/eliminar/es', methods=('GET', 'POST'))
@es_login_required_voluntario
def es_delete_voluntario(id):
    unico_voluntario(id)

    db = get_db()
    db.execute('DELETE FROM voluntario WHERE id = ?', (id,))
    db.commit()

    return redirect(url_for('auth.es_login_voluntario'))

# Visualização em português da função 'pt_workshop_voluntario' será apresentado as publicações que foram recém-criadas, as mais recentes estão em destaque primeiro
@bp.route('/dashboard/voluntario/workshop')
@pt_login_required_voluntario
def pt_workshop_voluntario():
    db = get_db()
    publicacoes = db.execute(
        "SELECT p.id, title, body, created, author_id, nome"
        " FROM workshop p JOIN voluntario v ON p.author_id = v.id"
        " ORDER BY created DESC"
    ).fetchall()

    return render_template('pt_br/dashboard/pt_workshop_voluntario_page.html', publicacoes=publicacoes)

# Visualização em espanhol da função 'es_workshop_voluntario' será apresentado as publicações que foram recém-criadas, as mais recentes estão em destaque primeiro
@bp.route('/dashboard/voluntario/workshop/es')
@es_login_required_voluntario
def es_workshop_voluntario():
    db = get_db()
    publicacoes = db.execute(
        "SELECT p.id, title, body, created, author_id, nome"
        " FROM workshop p JOIN voluntario v ON p.author_id = v.id"
        " ORDER BY created DESC"
    ).fetchall()

    return render_template('es_es/dashboard/es_workshop_voluntario_page.html', publicacoes=publicacoes)

# Visualização em português da função 'pt_create_workshop', servirá para o usuário Voluntário criar a sua própria publicação de Workshop
@bp.route('/dashboard/voluntario/workshop/publicar', methods=('GET', 'POST'))
@pt_login_required_voluntario
def pt_create_workshop():
    if request.method == 'POST':
        title = request.form['titulo']
        body = request.form['texto']
        error = None

        if not title:
            error = 'Por favor, o Título é obrigatório.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO workshop (title, body, author_id)"
                " VALUES (?, ?, ?)",
                (title, body, g.voluntario['id'])
            )
            db.commit()

            return redirect(url_for('dashboard.pt_workshop_voluntario'))

    return render_template('pt_br/dashboard/pt_workshop_p_voluntario_page.html')

# Visualização em espanhol da função 'es_create_workshop', servirá para o usuário Voluntário criar a sua própria publicação de Workshop
@bp.route('/dashboard/voluntario/workshop/publicar/es', methods=('GET', 'POST'))
@es_login_required_voluntario
def es_create_workshop():
    if request.method == "POST":
        title = request.form['titulo']
        body = request.form['texto']
        error = None

        if not title:
            error = 'Por favor, se require el Título.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO workshop (title, body, author_id)"
                " VALUES (?, ?, ?)",
                (title, body, g.voluntario['id'])
            )
            db.commit()

            return redirect(url_for('dashboard.es_workshop_voluntario'))

    return render_template('es_es/dashboard/es_workshop_p_voluntario_page.html')


# A função 'get_workshop', possibilita verificar se a determinada publicação de workshop é do autor,
# sendo útil, para utilizar na visualização de 'pt_update_workshop' e 'pt_delete_workshop'
def get_workshop(id, check_author=True):
    publicacao = get_db().execute(
        "SELECT p.id, title, body, created, author_id, nome"
        " FROM workshop p JOIN voluntario v ON p.author_id = v.id"
        " WHERE p.id = ?",
        (id,)
    ).fetchone()

    if publicacao is None:
        abort(404, f"Publicação de Workshop com id {id} não existe.")

    if check_author and publicacao['author_id'] != g.voluntario['id']:
        abort(403)

    return publicacao

# Visualização em português sobre a função 'pt_update_workshop', servirá para o usuário Voluntário editar a sua própria publicação de Workshop
@bp.route('/dashboard/voluntario/workshop/<int:id>/editar', methods=('GET', 'POST'))
@pt_login_required_voluntario
def pt_update_workshop(id):
    publicacao = get_workshop(id)

    if request.method == 'POST':
        title = request.form['titulo']
        body = request.form['texto']
        error = None

        if not title:
            error = 'Por favor, o Título é obrigatório.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE workshop SET title = ?, body = ?"
                " WHERE id = ?",
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('dashboard.pt_workshop_voluntario'))

    return render_template('pt_br/dashboard/pt_workshop_u_voluntario_page.html', publicacao=publicacao)

# Visualização em espanhol sobre a função 'es_update_workshop', servirá para o usuário Voluntário editar a sua própria publicação de Workshop
@bp.route('/dashboard/voluntario/workshop/<int:id>/editar/es', methods=('GET', 'POST'))
@es_login_required_voluntario
def es_update_workshop(id):
    publicacao = get_workshop(id)

    if request.method == 'POST':
        title = request.form['titulo']
        body = request.form['texto']
        error = None

        if not title:
            error = 'Por favor, se require el Título.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE workshop SET title = ?, body = ?"
                " WHERE id = ?",
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('dashboard.es_workshop_voluntario'))

    return render_template('es_es/dashboard/es_workshop_u_voluntario_page.html', publicacao=publicacao)

# Visualização em português sobre a função 'pt_delete_workshop', servirá para o usuário Voluntário remover a sua própria publicação de Workshop
@bp.route('/dashboard/voluntario/workshop/<int:id>/excluir', methods=('POST',))
@pt_login_required_voluntario
def pt_delete_workshop(id):
    get_workshop(id)

    db = get_db()
    db.execute('DELETE FROM workshop WHERE id = ?', (id,))
    db.commit()

    return redirect(url_for('dashboard.pt_workshop_voluntario'))

# Visualização em espanhol sobre a função 'es_delete_workshop', servirá para o usuário Voluntário remover a sua própria publicação de Workshop
@bp.route('/dashboard/voluntario/workshop/<int:id>/borrar/es', methods=('POST',))
@es_login_required_voluntario
def es_delete_workshop(id):
    get_workshop(id)

    db = get_db()
    db.execute('DELETE FROM workshop WHERE id= ?', (id,))
    db.commit()

    return redirect(url_for('dashboard.es_workshop_voluntario'))
