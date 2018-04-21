from flask import Flask

from app.api import api_rest, api_bp
from app.client import client_bp

app = Flask(__name__, static_url_path='')
app.register_blueprint(api_bp)
app.register_blueprint(client_bp)

from . import config
app.logger.info('>>> {}'.format(config.flask_config))
