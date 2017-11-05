""" Global Flask Application Settings """

import os
from genome import app


class Config(object):
    DEBUG = False
    TESTING = False
    PRODUCTION = False


class Development(Config):
    MODE = 'Development'
    DEBUG = True
    SECRET_KEY = 'SuperSecretKey'


class Production(Config):
    MODE = 'Production'
    DEBUG = False
    PRODUCTION = True
    # SECRET_KEY = os.environ['SECRET_KEY']


# Set FLASK_CONFIG env to 'Production' or 'Development' to set Config
flask_config = os.environ.get('FLASK_CONFIG', 'Development')
app.config.from_object('genome.config.{}'.format(flask_config))
