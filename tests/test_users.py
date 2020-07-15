import json


# TODO - modify tests to ensure someone with an email address that already exists, can't create an account again...

def test_logout_invalid(test_client):
    """
    Test logging out a user when they're not logged in
    """
    response = test_client.post('/logout')
    assert response.status_code == 401
    expected = {
        "message": "The server could not verify that you are authorized to access the URL requested. You either supplied the wrong credentials (e.g. a bad password), or your browser doesn't understand how to supply the credentials required."
    }
    assert expected == json.loads(response.get_data(as_text=True))


def test_register_user(test_client):
    """
    Test registering a user to the platform
    """
    mock_request_headers = {
        'Content-Type': 'application/json'
    }
    mock_request_data = {
	"name": "businessowner",
	"email": "businessowner@example.com",
    "password": "pass1234"
    }
    response = test_client.post('/register', data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 201
    expected = {
        "message": "SUCCESS_REGISTER_MESSAGE"
    }
    assert expected == json.loads(response.get_data(as_text=True))


def test_register_user_missing_details(test_client):
    """
    Test registering a user to the platform when they have not entered all details
    """
    mock_request_headers = {
        'Content-Type': 'application/json'
    }
    mock_request_data = {}
    response = test_client.post('/register', data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 400
    expected = {
        "email": [
            "Missing data for required field."
        ],
        "name": [
            "Missing data for required field."
        ],
        "password": [
            "Missing data for required field."
        ]
    }
    assert expected == json.loads(response.get_data(as_text=True))


def test_login_invalid_credentials(test_client):
    """
    Test logging a user in with incorrect password
    """
    mock_request_headers = {
        'Content-Type': 'application/json'
    }
    mock_request_data = {
	"email": "businessowner@example.com",
    "password": "pass12345"
    }
    response = test_client.post('/login', data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 401
    expected = {
        "message": "INVALID_CREDENTIALS"
    }
    assert expected == json.loads(response.get_data(as_text=True))
    
    """
    Test logging a user in with incorrect email address
    """
    mock_request_headers = {
        'Content-Type': 'application/json'
    }
    mock_request_data = {
	"email": "businessowner123@example.com",
    "password": "pass1234"
    }
    response = test_client.post('/login', data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 401
    expected = {
        "message": "INVALID_CREDENTIALS"
    }
    assert expected == json.loads(response.get_data(as_text=True))
    
    """
    Test logging a user in with name included in request
    """
    mock_request_headers = {
        'Content-Type': 'application/json'
    }
    mock_request_data = {
    "name": "businessowner",
	"email": "businessowner@example.com",
    "password": "pass1234"
    }
    response = test_client.post('/login', data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 400
    expected = {
        "name": [
            "Unknown field."
        ]
    }
    assert expected == json.loads(response.get_data(as_text=True))


# TODO test return of a cookie <- this may not be needed when we have JWT working & have removed flask-login
# TODO test return of JWT
def test_login(test_client):
    """
    Test logging a user into to the platform
    """
    mock_request_headers = {
        'Content-Type': 'application/json'
    }
    mock_request_data = {
	"email": "businessowner@example.com",
    "password": "pass1234"
    }
    response = test_client.post('/login', data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 200
    # expected = {
    #     "message": "SUCCESS_REGISTER_MESSAGE"
    # }
    # assert expected == json.loads(response.get_data(as_text=True))


def test_logout(test_client):
    """
    Test logging out a user when they're logged in
    """
    response = test_client.post('/logout')
    assert response.status_code == 200
    expected = {
        "message": "LOGGED_OUT"
    }
    assert expected == json.loads(response.get_data(as_text=True))


