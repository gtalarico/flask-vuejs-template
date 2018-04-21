""" API Backend - Base Resource Models """

from flask_restplus import Resource, abort

from app.api.security import require_auth


class BaseResource(Resource):

    def get(self, *args, **kwargs):
        abort(405)

    def post(self, *args, **kwargs):
        abort(405)

    def put(self, *args, **kwargs):
        abort(405)

    def patch(self, *args, **kwargs):
        abort(405)

    def delete(self, *args, **kwargs):
        abort(405)

class SecureResource(BaseResource):
    method_decorators = [require_auth]
