from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Hello, CI/CD Pipeline!"

def test_time():
    client = app.test_client()
    response = client.get('/time')
    assert response.status_code == 200
    assert b"Current time is:" in response.data
