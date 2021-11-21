from flask import (
    flash, Blueprint, request, render_template, redirect, url_for, g, session
)

from werkzeug.security import check_password_hash, generate_password_hash

from imu.db import get_db

bp = Blueprint('auth', __name__)

# Visualização em português sobre a página que contém o formulário de registro para o usuário Refugiado, com a função 'pt_cadastro_refugiado'
@bp.route('/cadastrar/refugiado/', methods=('GET', 'POST'))
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
@bp.route('/cadastrar/voluntario/', methods=('GET', 'POST'))
def pt_cadastro_voluntario():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        nacionalidade = request.form['nacionalidade']
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
                    "INSERT INTO voluntario (nome, sobrenome, nacionalidade, email, senha) VALUES (?, ?, ?, ?, ?)",
                    (nome, sobrenome, nacionalidade, email, generate_password_hash(senha)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"O Usuário com {email} já está registrado."
            else:
                return redirect(url_for("auth.pt_login_voluntario"))

        flash(error)

    return render_template('pt_br/cadastrar/cadastrar_voluntario_page.html')

#Foi definido essa rota de login para refugiado.
@bp.route('/login/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['username']
        senha = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM refugiado WHERE email = ?', (email,)
        ).fetchone()

        if user is None:
            error = 'Usarname Incorreto.'
        elif not check_password_hash(user['senha'], senha):
            error = 'Senha Incorreto.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('login.html')

#Foi definido essa rota de login para voluntario.
@bp.route('/login_voluntario/', methods=('GET', 'POST'))
def login_voluntario():
    if request.method == 'POST':
        email = request.form['username']
        senha = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM voluntario WHERE email = ?', (email,)
        ).fetchone()

        if user is None:
            error = 'Usarname Incorreto.'
        elif not check_password_hash(user['senha'], senha):
            error = 'Senha Incorreto.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('login_voluntario.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
