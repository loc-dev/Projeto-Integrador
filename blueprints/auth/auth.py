# 05 - Criando o Blueprint de Autenticação (Cadastro de Refugiado e Voluntário, Login de Refugiado e Voluntário)

import functools

from flask import (
    flash, Blueprint, request, render_template, redirect, url_for, g, session
)

from werkzeug.security import check_password_hash, generate_password_hash

from imu.db import get_db

bp = Blueprint('auth', __name__)

# Visualização em português sobre a página que contém o formulário de registro para o usuário Refugiado, com a função 'pt_cadastro_refugiado'
@bp.route('/cadastrar/refugiado', methods=('GET', 'POST'))
def pt_cadastro_refugiado():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        nacionalidade = request.form['nacionalidade']
        email = request.form['email']
        senha = request.form['senha']
        db = get_db()
        error = None

        if  not nome and not email and not senha:
            error = 'Por favor, os campos com ( * ) são obrigatórios!'
        elif not email and not senha:
            error = 'Por favor, o E-mail e Senha são obrigatórios!'
        elif not nome:
            error = 'Por favor, o Nome é obrigatório.'
        elif not email:
            error = 'Por favor, o E-mail é obrigatório.'
        elif not senha:
            error = 'Por favor, a Senha é obrigatório.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO refugiado (nome, sobrenome, nacionalidade, email, senha) VALUES (?, ?, ?, ?, ?)",
                    (nome, sobrenome, nacionalidade, email, generate_password_hash(senha)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"O Usuário com {email} já está registrado."
            else:
                return redirect(url_for("auth.pt_login_refugiado"))

        flash(error)

    return render_template('pt_br/cadastrar/cadastrar_refugiado_page.html')

# Visualização em espanhol sobre a página que contém o formulário de registro para o usuário Refugiado, com a função 'es_cadastro_refugiado'
@bp.route('/registrar/refugiado/es', methods=('GET', 'POST'))
def es_cadastro_refugiado():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        nacionalidade = request.form['nacionalidade']
        email = request.form['email']
        senha = request.form['senha']
        db = get_db()
        error = None

        if  not nome and not email and not senha:
            error = '¡Por favor, los campos con (*) son obligatorios!'
        elif not email and not senha:
            error = '¡Por favor, el correo electrónico y contraseña son obligatorios!'
        elif not nome:
            error = '¡Por favor, se requiere nombre!'
        elif not email:
            error = '¡Por favor, se require correo electrónico!'
        elif not senha:
            error = '¡Por favor, se require contraseña!'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO refugiado (nome, sobrenome, nacionalidade, email, senha) VALUES (?, ?, ?, ?, ?)",
                    (nome, sobrenome, nacionalidade, email, generate_password_hash(senha)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"El usuario con {email} ya esta registrado."
            else:
                return redirect(url_for("auth.es_login_refugiado"))

        flash(error)

    return render_template('es_es/cadastrar/cadastrar_refugiado_page_es.html')

# Visualização em português sobre a página que contém o formulário de registro para o usuário Voluntário, com a função 'pt_cadastro_voluntario'
@bp.route('/cadastrar/voluntario', methods=('GET', 'POST'))
def pt_cadastro_voluntario():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        senha = request.form['senha']
        db = get_db()
        error = None

        if not nome and not email and not senha:
            error = 'Por favor, os campos com ( * ) são obrigatórios!'
        elif not email and not senha:
            error = 'Por favor, o E-mail e Senha são obrigatórios!'
        elif not nome:
            error = 'Por favor, o Nome é obrigatório.'
        elif not email:
            error = 'Por favor, o E-mail é obrigatório.'
        elif not senha:
            error = 'Por favor, a Senha é obrigatório.'
        
        if error is None:
            try:
                db.execute(
                    "INSERT INTO voluntario (nome, sobrenome, email, senha) VALUES (?, ?, ?, ?)",
                    (nome, sobrenome, email, generate_password_hash(senha)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"O Usuário com {email} já está registrado."
            else:
                return redirect(url_for("auth.pt_login_voluntario"))

        flash(error)

    return render_template('pt_br/cadastrar/cadastrar_voluntario_page.html')

# Visualização em espanhol sobre a página que contém o formulário de registro para o usuário Voluntário, com a função 'es_cadastro_voluntario'
@bp.route('/cadastrar/voluntario/es', methods=('GET', 'POST'))
def es_cadastro_voluntario():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        senha = request.form['senha']
        db = get_db()
        error = None

        if not nome and not email and not senha:
            error = '¡Por favor, los campos con (*) son obligatorios!'
        elif not email and not senha:
            error = '¡Por favor, el correo electrónico y contraseña son obligatorios!'
        elif not nome:
            error = '¡Por favor, se requiere nombre!'
        elif not email:
            error = '¡Por favor, se require correo electrónico!'
        elif not senha:
            error = '¡Por favor, se require contraseña!'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO voluntario (nome, sobrenome, email, senha) VALUES (?, ?, ?, ?)",
                    (nome, sobrenome, email, generate_password_hash(senha)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"El usuario con {email} ya esta registrado."
            else:
                return redirect(url_for("auth.es_login_voluntario"))

        flash(error)

    return render_template('es_es/cadastrar/cadastrar_voluntario_page_es.html')

# Visualização em português sobre a página que contém o formulário de login para o usuário Refugiado, com a função 'pt_login_refugiado'
@bp.route('/login/refugiado', methods=('GET', 'POST'))
def pt_login_refugiado():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        db = get_db()
        error = None
        refugiado = db.execute(
            "SELECT * FROM refugiado WHERE email = ?", (email,)
        ).fetchone()

        if refugiado is None:
            error = 'E-mail está incorreto!'
        elif not check_password_hash(refugiado['senha'], senha):
            error = 'Senha está incorreta!'

        if error is None:
            session.clear()
            session['refugiado_id'] = refugiado['id']
            return redirect(url_for('dashboard.pt_index_refugiado'))

        flash(error)

    return render_template('pt_br/login/login_refugiado_page.html')

# Visualização em espanhol sobre a página que contém o formulário de login para o usuário Refugiado, com a função 'es_login_refugiado'
@bp.route('/login/refugiado/es', methods=('GET', 'POST'))
def es_login_refugiado():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        db = get_db()
        error = None
        refugiado = db.execute(
            "SELECT * FROM refugiado WHERE email = ?", (email,)
        ).fetchone()

        if refugiado is None:
            error = '¡El correo electrónico es incorrecto!'
        elif not check_password_hash(refugiado['senha'], senha):
            error = '¡La contraseña es incorrecta!'

        if error is None:
            session.clear()
            session['refugiado_id'] = refugiado['id']
            return redirect(url_for('dashboard.es_index_refugiado'))

        flash(error)

    return render_template('es_es/login/login_refugiado_page_es.html')

# Visualização em português sobre a página que contém o formulário de login para o usuário Voluntário, com a função 'pt_login_voluntario'
@bp.route('/login/voluntario', methods=('GET', 'POST'))
def pt_login_voluntario():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        db = get_db()
        error = None
        voluntario = db.execute(
            "SELECT * FROM voluntario WHERE email = ?", (email,)
        ).fetchone()

        if voluntario is None:
            error = 'E-mail está incorreto!'
        elif not check_password_hash(voluntario['senha'], senha):
            error = 'Senha está incorreta!'
        
        if error is None:
            session.clear()
            session['voluntario_id'] = voluntario['id']
            return redirect(url_for('dashboard.pt_index_voluntario'))

        flash(error)

    return render_template('pt_br/login/login_voluntario_page.html')

# Visualização em espanhol sobre a página que contém o formulário de login para o usuário Voluntário, com a função 'es_login_voluntario'
@bp.route('/login/voluntario/es', methods=('GET', 'POST'))
def es_login_voluntario():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        db = get_db()
        error = None
        voluntario = db.execute(
            "SELECT * FROM voluntario WHERE email = ?", (email,)
        ).fetchone()

        if voluntario is None:
            error = "¡El correo electrónico es incorrecto!"
        elif not check_password_hash(voluntario['senha'], senha):
            error = "¡La contraseña es incorrecta!"

        if error is None:
            session.clear()
            session['voluntario_id'] = voluntario['id']
            return redirect(url_for('dashboard.es_index_voluntario'))

        flash(error)

    return render_template('es_es/login/login_voluntario_page_es.html')

# Função para ser executada antes de uma função de visualização ou até fora do Blueprint, irá funcionar para ambas versões de idioma, sendo somente o usuário Refugiado
@bp.before_app_request
def load_logged_in_refugiado():
    refugiado_id = session.get('refugiado_id')

    if refugiado_id is None:
        g.refugiado = None
    else:
        g.refugiado = get_db().execute(
            "SELECT * FROM refugiado WHERE id = ?", (refugiado_id,)
        ).fetchone()

# Função para ser executada antes de uma função de visualização ou até fora do Blueprint, irá funcionar para ambas versões de idioma, sendo somente o usuário Voluntário
@bp.before_app_request
def load_logged_in_voluntario():
    voluntario_id = session.get('voluntario_id')

    if voluntario_id is None:
        g.voluntario = None
    else:
        g.voluntario = get_db().execute(
            "SELECT * FROM voluntario WHERE id = ?",
            (voluntario_id,)
        ).fetchone()

# Função para o refugiado que estiver na página Dashboard em português, encerrar a sua sessão, retornar para página de Login em português
@bp.route('/refugiado/logout')
def pt_logout_refugiado():
    session.clear()

    return redirect(url_for('auth.pt_login_refugiado'))

# Função para o voluntário que estiver na página Dashboard em português, encerrar a sua sessão, retornar para página de Login em português
@bp.route('/voluntario/logout')
def pt_logout_voluntario():
    session.clear()

    return redirect(url_for('auth.pt_login_voluntario'))

# Função para exigir autenticação em outras visualizações, nesse caso, para o usuário refugiado
def pt_login_required_refugiado(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.refugiado is None:
            return redirect(url_for('auth.pt_login_refugiado'))

        return view(**kwargs)

    return wrapped_view

# Função para exigir autenticação em outras visualizações, nesse caso, para o usuário voluntário
def pt_login_required_voluntario(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.voluntario is None:
            return redirect(url_for('auth.pt_login_voluntario'))

        return view(**kwargs)

    return wrapped_view

# Função para o refugiado que estiver na página Dashboard em espanhol, encerrar a sua sessão, retornar para página de Login em espanhol
@bp.route('refugiado/encerrar')
def es_logout_refugiado():
    session.clear()

    return redirect(url_for('auth.es_login_refugiado'))

# Função para o voluntario que estiver na página Dashboard em espanhol, encerrar a sua sessão, retornar para página de Login em espanhol
@bp.route('voluntario/encerrar')
def es_logout_voluntario():
    session.clear()

    return redirect(url_for('auth.es_login_voluntario'))

# Função para exigir autenticação em outras visualizações que estão no idioma espanhol, nesse caso, para o usuário refugiado
def es_login_required_refugiado(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.refugiado is None:
            return redirect(url_for('auth.es_login_refugiado'))

        return view(**kwargs)

    return wrapped_view

# Função para exigir autenticação em outras visualizações que estão no idioma espanhol, nesse caso, para o usuário voluntario
def es_login_required_voluntario(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.voluntario is None:
            return redirect(url_for('auth.es_login_voluntario'))

        return view(**kwargs)
    
    return wrapped_view
