import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.json['message'] == 'Welcome to test-lt'

def test_login_page(client):
    resp = client.get('/login')
    assert resp.status_code == 200
    assert b'\xe7\x99\xbb\xe5\xbd\x95' in resp.data
