""" Security Related things """
from functools import wraps
from flask_restful import abort

def require_auth(func):
    """ Secure method decorator """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Verify if User is Authenticated
        if True:
            return abort(401)
        else:
            return func(*args, **kwargs)
    return wrapper
