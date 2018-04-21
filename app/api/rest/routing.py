"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

import time
from flask import request
from flask_restplus import Api

from app.api.rest.base import BaseResource, SecureResource
from app.api import api_rest


@api_rest.route('/resource/<string:resource_id>')
class ResourceOne(BaseResource):
    """ Sample Resource Class """

    def get(self, resource_id):
        time.sleep(1)
        return {'resource_id': resource_id}

    def post(self, resource_id):
        json_payload = request.json
        return {'resource': json_payload}, 201


@api_rest.route('/secure-resource/<string:resource_id>')
class SecureResourceOne(SecureResource):

    def get(self, resource_id):
        return {'resource_id': resource_id}
