""" pytests for Flask """

import pytest
from app import app

@pytest.fixture(scope="module")
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_api(client):
    resp = client.get('/api/')
    assert resp.status_code == 200

def test_resource_one(client):
    resp = client.get('/api/resource/one')
    assert resp.status_code == 200

def test_resource_one_post(client):
    resp = client.post('/api/resource/one')
    assert resp.status_code == 201

def test_resource_one_patch(client):
    resp = client.patch('/api/resource/one')
    assert resp.status_code == 405

def test_secure_resource_fail(client):
    resp = client.get('/api/secure-resource/two')
    assert resp.status_code == 401

def test_secure_resource_pass(client):
    resp = client.get('/api/secure-resource/two',
                      headers={'authorization': 'Bearer x'})
    assert resp.status_code == 200

@pytest.fixture(scope="module")
def request_context():
    return app.test_request_context('')

def test_session(request_context):
    with request_context:
        # Do something that requires request context
        assert True
