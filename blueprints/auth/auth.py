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

# Visualização em espanhol sobre a página que contém o formulário de registro para o usuário Voluntário, com a função 'es_cadastro_voluntario'
@bp.route('/cadastrar/voluntario/es', methods=('GET', 'POST'))
def es_cadastro_voluntario():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        nacionalidade = request.form['nacionalidade']
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
                    "INSERT INTO voluntario (nome, sobrenome, nacionalidade, email, senha) VALUES (?, ?, ?, ?, ?)",
                    (nome, sobrenome, nacionalidade, email, generate_password_hash(senha)),
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
            return redirect(url_for('index'))

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
            return redirect(url_for('index'))

        flash(error)

    return render_template('es_es/login/login_refugiado_page_es.html')

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
