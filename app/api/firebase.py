import io
import os
from google.oauth2 import service_account
from flask import request
from flask_restplus import Resource
import firebase_admin
from firebase_admin import db,credentials
# from app import db
import flask
from .security import require_auth
from . import api_rest

app = flask.Flask(__name__)
# app = Flask(__name__)

cred = credentials.Certificate("/Users/shahnawaz/Documents/ml/ML Course/Week10/tripive/keys/tripive-firebase-adminsdk-zoa3q-3aac541827.json")
firebase_admin.initialize_app(cred,options={
    'databaseURL': 'https://tripvive.firebaseio.com'
})


class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]

SUPERHEROES = db.reference('tripive')

@app.route('/heroes/<string:resource_id>', methods=['POST'])
class SecureResourceTwo(Resource):
    """ Unsecure Resource Class: Inherit from Resource """
    def create_hero():
        req = flask.request.json
        hero = SUPERHEROES.push(req)
        return flask.jsonify({'id': hero.key}), 201

@app.route('/heroes/<id>')
def read_hero(id):
    return flask.jsonify(_ensure_hero(id))

@app.route('/heroes/<id>', methods=['PUT'])
def update_hero(id):
    _ensure_hero(id)
    req = flask.request.json
    SUPERHEROES.child(id).update(req)
    return flask.jsonify({'success': True})

@app.route('/heroes/<id>', methods=['DELETE'])
def delete_hero(id):
    _ensure_hero(id)
    SUPERHEROES.child(id).delete()
    return flask.jsonify({'success': True})

def _ensure_hero(id):
    hero = SUPERHEROES.child(id).get()
    if not hero:
        flask.abort(404)
    return hero

# @api_rest.route('/demo')
# # class SecureResourceTwo(Resource):
#     """ Unsecure Resource Class: Inherit from Resource """

# def get(self,resource_id):
#         # timestamp = datetime.utcnow().isoformat()
#         return {'timestamp': 'Hello World'}     

@app.route('/demo')                     #Working
def demo_hero():
    return {'timestamp': 'Hello World'}     

@app.route('/demos/<id>', methods=['POST']) #Not Working
def democ_hero():
        req = flask.request.json
        hero = SUPERHEROES.push(req)
        return flask.jsonify({'id': hero.key}), 201    