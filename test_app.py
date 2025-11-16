# test_app.py
import app


def test_hello():
    client = app.app.test_client()
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}


def test_echo():
    client = app.app.test_client()
    payload = {"msg": "ping"}
    response = client.post('/echo', json=payload)
    assert response.status_code == 201
    assert response.get_json() == payload


def test_reverse():
    client = app.app.test_client()
    payload = {"text": "hello"}
    response = client.post('/reverse', json=payload)
    assert response.status_code == 201
    assert response.get_json() == {"reversed_text": "olleh"}


def test_square():
    client = app.app.test_client()
    response = client.get('/square/4')
    assert response.status_code == 200
    assert response.get_json() == {"square": 16}
