import io
import os
from google.oauth2 import service_account

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth
from firebase_admin import firestore
# from app import db
from flask import request,jsonify
from flask_restplus import Resource,reqparse, Api
import flask
import json 
from .security import require_auth
from . import api_rest
# from .config import Config
from dotenv import load_dotenv
load_dotenv('.flaskenv')

app = flask.Flask(__name__)
# api = Api(app)

# parser = reqparse.RequestParser()

cred = credentials.Certificate(os.getenv('FIREBASE_ADMIN_CRED'))

# Initialize the app with a service account, granting admin privileges
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://tripive.firebaseio.com'
# })

firebase_admin.initialize_app(cred)

db = firestore.client()

class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]

# SUPERHEROES = db.reference('refimages')
# print(SUPERHEROES.get())

@app.route('/heroes/<string:resource_id>',methods=['POST'])
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

def _ensure_hero(id):                                       #We can write a function here to query
    hero = SUPERHEROES.child(id).get()
    if not hero:
        flask.abort(404)
    return hero

@api_rest.route('/demo/<string:resource_id>')
class CallDemoGetRequest(Resource):
    
    def get(self, resource_id):
        # timestamp = datetime.utcnow().isoformat()
        # query = SUPERHEROES.order_by_child('name').equal_to(resource_id).get()
        # return jsonify(_ensure_hero(resource_id))
        # snapshot = SUPERHEROES.child('name').get()
        # print(snapshot)
        # for key, val in snapshot.items():
        #     print('{0} was {1} meters tall'.format(key, val))
        # # Create a query against the collection
        # query_ref = cities_ref.where(u'name', u'==', u'Spider-Man3')
        # print(query_ref)
        # ref.orderByChild("height").equalTo(25).on("child_added", function(snapshot) {
        #     console.log(snapshot.key);
        # })
        return {'test':'SUCESSS'}

    def post(self, resource_id):
        json_payload = request.json
        print(json_payload)
        hero = SUPERHEROES.push(json_payload)
        return {'id': hero.key}, 201

# Reference https://firebase.google.com/docs/firestore/query-data/get-data
@api_rest.route('/firedb/<string:resource_id>')
class CallDemoGetRequest(Resource):
    
    def get(self, resource_id):
        data = {}
        doc_ref = db.collection('intialimageref')
        docs = doc_ref.stream()
    
        for doc in docs:
            rowdata = {doc.id: doc.to_dict()}
            data.update(rowdata)
        print(data)

        return {'images':data}

    def post(self, resource_id):
        json_payload = request.json
        doc_ref = db.collection('intialimageref').document(resource_id)         #Creating document for each labels
        doc_ref.set(json_payload)
        return {'message': 'success'}, 201        