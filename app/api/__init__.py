""" API Blueprint Application """

from flask import Blueprint, current_app
from flask_restplus import Api
# import firebase_admin
# from firebase_admin import db,credentials

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')
api_rest = Api(api_bp)

# cred = credentials.Certificate("/Users/shahnawaz/Documents/ml/ML Course/Week10/tripive/keys/tripive-firebase-adminsdk-zoa3q-3aac541827.json")
# firebase_admin.initialize_app(cred,options={
#     'databaseURL': 'https://tripvive.firebaseio.com'
# })

@api_bp.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response


# Import resources to ensure view is registered
from .resources import * # NOQA
# from .vision import *
from .firebase import *
