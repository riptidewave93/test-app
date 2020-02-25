from app import app
import pytest

def test_get_world():
    response = app.test_client().get('/world')

    assert response.status_code == 200
    assert response.data == b'Hello world!'

def test_get_john():
    response = app.test_client().get('/john')

    assert response.status_code == 200
    assert response.data == b'Hello john!'

def test_get_world_es():
    response = app.test_client().get('/world?lang=es')

    assert response.status_code == 200
    assert response.data == b'Hola world!'

def test_get_john_es():
    response = app.test_client().get('/john?lang=es')

    assert response.status_code == 200
    assert response.data == b'Hola john!'

def test_get_json_world():
    response = app.test_client().get('/world', headers={'Accept': 'application/json'})

    assert response.status_code == 200
    assert response.json['msgs'] == ["Hello world!"]

def test_get_json_john():
    response = app.test_client().get('/john', headers={'Accept': 'application/json'})

    assert response.status_code == 200
    assert response.json['msgs'] == ["Hello john!"]

def test_get_json_john_es():
    response = app.test_client().get('/john?lang=es', headers={'Accept': 'application/json'})

    assert response.status_code == 200
    assert response.json['msgs'] == ["Hola john!"]

def test_get_json_world_es():
    response = app.test_client().get('/world?lang=es', headers={'Accept': 'application/json'})

    assert response.status_code == 200
    assert response.json['msgs'] == ["Hola world!"]
