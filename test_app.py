from app import app
import pytest

def test_get():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'<p>Hello, World</p>'

def test_get_json():
    response = app.test_client().get('/', headers={'Accept': 'application/json'})

    assert response.status_code == 200
    assert response.json['message'] == "Hello, World"

def test_post():
    response = app.test_client().post('/')

    assert response.status_code == 200
    assert response.data == b'<p>Hello, World</p>'

def test_bad_methods():
    response = app.test_client().delete('/')

    assert response.status_code == 405

    response = app.test_client().patch('/')

    assert response.status_code == 405
