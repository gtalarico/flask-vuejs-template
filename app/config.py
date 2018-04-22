""" Global Flask Application Settings """

import os
from app import app


class Config(object):
    DEBUG = False
    TESTING = False
    BASE_DIR = os.path.dirname(__file__)
    CLIENT_DIR = os.path.join(BASE_DIR, 'client', 'vue_app')

    if not os.path.exists(CLIENT_DIR):
        raise Exception(
            'Client App directory not found: {}'.format(CLIENT_DIR))


class Development(Config):
    DEBUG = True
    PRODUCTION = False
    SECRET_KEY = 'SuperSecretKey'


class Production(Config):
    DEBUG = False
    PRODUCTION = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'UnsafeSecret')


# Set `FLASK_CONFIG` env to 'Production' or 'Development' to set Config
flask_config = os.environ.get('FLASK_CONFIG', 'Development')
app.config.from_object('app.config.{}'.format(flask_config))
