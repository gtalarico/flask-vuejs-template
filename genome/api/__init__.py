""" API Blueprint Application """

import os
from flask import Flask, Blueprint, session
from flask_restful import Api

api_bp = Blueprint('api_app', __name__,
                   template_folder='templates',
                   url_prefix='/api')

api_rest = Api(api_bp)

@api_bp.after_request
def add_header(response):
    # Required for vue app served from localhost to access 127.0.0.1:5000
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

from genome.api import views
from genome.api.rest import routing

