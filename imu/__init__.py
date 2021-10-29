# 01 - Estabelecendo a nossa fábrica de aplicativos.

import os

from flask import Flask

# Definição das configurações para o aplicativo imu.
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'imu.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/ola")
    def hello():
        return 'Ola'

    # Importando o nosso Banco de Dados da raíz do pacote imu, e, chamando as funções para o aplicativo.
    from . import db
    db.init_app(app)

    # Importando o Blueprint 'lang' da pasta fora da raíz do pacote imu.
    from blueprints.lang import lang
    app.register_blueprint(lang.bp)

    return app
