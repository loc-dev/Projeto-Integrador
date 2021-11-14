from flask import (
    flash, Blueprint, request, render_template, redirect, url_for, g, session
)

from werkzeug.security import check_password_hash, generate_password_hash

from imu.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register/', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if  not username and not password:
            error = 'Insira Usuário e Senha!'
        elif not username:
            error = 'Insira Usuário.'
        elif not password:
            error = 'Insira Senha.'        


        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"Usuario {username} já esta registrado."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('register.html')


@bp.route('/login/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Usarname Incorreto.'
        elif not check_password_hash(user['password'], password):
            error = 'Senha Incorreto.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('login.html')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
