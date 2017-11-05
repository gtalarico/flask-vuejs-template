"""
REST API Resource Routing

http://flask-restful.readthedocs.io/en/latest/
"""

import time
from flask import request
from genome.api.rest.base import BaseResource, SecureResource, rest_resource

@rest_resource
class ResourceOne(BaseResource):
    """ /api/resource/one """
    endpoints = ['/resource/one']

    def get(self):
        time.sleep(1)
        return {'name': 'Resource One', 'data': True}

    def post(self):
        json_payload = request.json
        return {'name': 'Resource Post'}


@rest_resource
class SecureResourceOne(SecureResource):
    """ /api/resource/two """
    endpoints = ['/resource/two/<string:resource_id>']

    def get(self, resource_id):
        time.sleep(1)
        return {'name': 'Resource Two', 'data': resource_id}

