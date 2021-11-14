from flask import (
    flash, Blueprint, request, render_template, redirect, url_for, g, session
)

from werkzeug.security import check_password_hash, generate_password_hash

from imu.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

#Foi definido essa rota para cadastro do refugiado.
@bp.route('/register/', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.form['username']
        senha = request.form['password']
        db = get_db()
        error = None

        if  not email and not senha:
            error = 'Insira Usuário e Senha!'
        elif not email:
            error = 'Insira Usuário.'
        elif not senha:
            error = 'Insira Senha.'        


        if error is None:
            try:
                db.execute(
                    "INSERT INTO refugiado (email, senha) VALUES (?, ?)",
                    (email, generate_password_hash(senha)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"Usuario {email} já esta registrado."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('register.html')

#Foi definido essa rota para cadastro do voluntário.
@bp.route('/register_voluntario/', methods=('GET', 'POST'))
def register_voluntario():
    if request.method == 'POST':
        email = request.form['username']
        senha = request.form['password']
        db = get_db()
        error = None

        if  not email and not senha:
            error = 'Insira Usuário e Senha!'
        elif not email:
            error = 'Insira Usuário.'
        elif not senha:
            error = 'Insira Senha.'        


        if error is None:
            try:
                db.execute(
                    "INSERT INTO voluntario (email, senha) VALUES (?, ?)",
                    (email, generate_password_hash(senha)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"Usuario {email} já esta registrado."
            else:
                return redirect(url_for("auth.login_voluntario"))

        flash(error)

    return render_template('register.html')

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
