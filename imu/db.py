# 02 - Definindo a Conexão, para realizar consultas e outras operações com banco de dados.

import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

# Estabelecendo a conexão
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

# A função 'close_db', irá verificar a conexão, para, posteriormente, fechar a conexão
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# Inicializando o Banco de Dados
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf-8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Executado com sucesso')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
