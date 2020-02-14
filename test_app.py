from app import app
import pytest

def test_get():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'<p>Hello, World</p>'

def test_get_json():
    response = app.test_client().get('/', headers={'Accept': 'application/json'})

    assert response.status_code == 200
    assert response.data == b'{"message": "Hello, World"}'

def test_post():
    response = app.test_client().post('/')

    assert response.status_code == 200
    assert response.data == b'<p>Hello, World</p>'
