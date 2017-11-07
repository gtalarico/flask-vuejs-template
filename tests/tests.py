""" pytests for Flask """

import pytest
from app import app

@pytest.fixture(scope="module")
def client():
    app.config['TESTING'] = True
    return app.test_client()

@pytest.fixture(scope="module")
def request_context():
    return app.test_request_context('')

def test_session(request_context):
    with request_context:
        # Do something that requires request context
        assert True

def test_two():
    assert True
