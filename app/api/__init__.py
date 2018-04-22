""" API Blueprint Application """

import os
from flask import Flask, Blueprint, session
from flask_restplus import Api

api_bp = Blueprint('api_bp', __name__,
                   template_folder='templates',
                   url_prefix='/api')

api_rest = Api(api_bp)

@api_bp.after_request
def add_header(response):
    # Required for Webpack dev served page to make api requests to flask
    # This is for development only
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

from app.api import views
from app.api.rest import routing
