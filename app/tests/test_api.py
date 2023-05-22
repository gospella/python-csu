from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_redirect():
    response = client.get('/')
    assert response.history[0].status_code == 307, response.text
    assert response.status_code == 200, response.text
    with open('src/templates/login.html', 'r') as f:
        assert response.text == f.read()

def test_login_page():
    response = client.get('/login')
    assert response.status_code == 200, response.text
    with open('src/templates/login.html', 'r') as f:
        assert response.text == f.read()
    
def test_form(user):
    form_data = {'username': user.username, 'password': user.password}
    response = client.post('/form', data=form_data)
    assert response.status_code == 200, response.text
    
    fake_form_data = {'username': user.username, 'password': 'asdv12312'}
    response = client.post('/form', data=fake_form_data)
    assert response.status_code == 403, response.text
    assert response.json()['detail'] == 'Incorrect login or password'