import flask
from flask import Flask
from flask_cas import CAS, login_required

import config


def init_app():
    app = Flask(__name__)
    app.cas = CAS(app, '/cas')
    app.secret_key = config.APP_SECRET
    app.config['CAS_SERVER'] = config.CAS_SERVER
    app.config['CAS_LOGIN_ROUTE'] = config.CAS_LOGIN_ROUTE
    app.config['CAS_LOGOUT_ROUTE'] = config.CAS_LOGOUT_ROUTE
    app.config['CAS_VALIDATE_ROUTE'] = config.CAS_VALIDATE_ROUTE
    app.config['CAS_AFTER_LOGIN'] = 'details'
    return app


app = init_app()


@app.route('/')
def index():
    return flask.render_template('index.html', cas=app.cas)


@app.route('/details')
@login_required
def details():
    return flask.render_template('details.html', cas=app.cas)
