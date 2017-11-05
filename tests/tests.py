""" pytests for Flask """

import pytest
import genome


@pytest.fixture(scope="module")
def client():
    genome.app.config['TESTING'] = True
    return genome.app.test_client()

@pytest.fixture(scope="module")
def request_context():
    return genome.app.test_request_context('')

def test_session(request_context):
    with request_context:
        # Do something that requires request context
        assert True

def test_two():
    assert True
