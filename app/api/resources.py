"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from datetime import datetime
from flask import request
from flask import jsonify
from flask_restplus import Resource
import flask
from .security import require_auth
from . import api_rest

###########

###########


class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]


@api_rest.route('/resource/<string:resource_id>')
class ResourceOne(Resource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}

    def post(self, resource_id):
        json_payload = request.json
        print(json_payload)
        return {'timestamp': json_payload}, 201

@api_rest.route('/secure-resource/<string:resource_id>')
class SecureResourceOne(SecureResource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}


# @api_rest.route('/demo/<string:resource_id>')
# class SecureResourceTwo(Resource):
#     """ Unsecure Resource Class: Inherit from Resource """

#     def get(self,resource_id):
#         # timestamp = datetime.utcnow().isoformat()
#         return {'timestamp': 'Hello World'}        
