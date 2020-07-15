import json


# TODO add requirements to be logged in...

def test_get_stores_is_empty(test_client):
    """
    Test that there are no stores in the DB
    """
    response = test_client.get('/stores')
    assert response.status_code == 200
    expected = {'stores': []}
    assert expected == json.loads(response.get_data(as_text=True))


def test_post_store_succeeds(test_client):
    """
    Test POST request creates a store
    """
    mock_request_headers = {
        'Content-Type': 'application/json'
    }
    mock_request_data = {
	"name": "Store 1",
	"description": "Store 1",
    }
    response = test_client.post('/store', data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 201
    expected = {'message': 'STORE_CREATED'}
    assert expected == json.loads(response.get_data(as_text=True))


def test_patch_store_succeeds(test_client):
    mock_request_headers = {
        'Content-Type': 'application/json'
    }
    mock_request_data = {
   	"name": "Store 1A",
	"description": "Store 1A",
    }
    response = test_client.patch('/store/1', data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 200
    expected = {
        "id": 1,
        "name": "Store 1A",
        "description": "Store 1A"
    }
    assert expected == json.loads(response.get_data(as_text=True))


def test_patch_store_not_found(test_client):
    mock_request_headers = {
        'Content-Type': 'application/json'
    }
    mock_request_data = {
   	"name": "Store 1A",
	"description": "Store 1A",
    }
    response = test_client.patch('/store/2', data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 404
    expected = {'message': 'STORE_NOT_FOUND'}
    assert expected == json.loads(response.get_data(as_text=True))


def test_get_stores(test_client):
    """
    Test getting list of Stores
    """
    response = test_client.get('/stores')
    assert response.status_code == 200
    expected = {
        "stores": [
            {
                "id": 1,
                "name": "Store 1A",
                "description": "Store 1A",
            }
        ]
    }
    assert expected == json.loads(response.get_data(as_text=True))


def test_get_store(test_client):
    """
    Test getting a single store
    """
    response = test_client.get('/store/1')
    assert response.status_code == 200
    expected = {
        "id": 1,
        "name": "Store 1A",
        "description": "Store 1A"
    }
    assert expected == json.loads(response.get_data(as_text=True))


def test_get_store_not_found(test_client):
    """
    Test getting a single store that doesn't exist
    """
    response = test_client.get('/store/2')
    assert response.status_code == 404
    expected = {"message": "STORE_NOT_FOUND"}
    assert expected == json.loads(response.get_data(as_text=True))


def test_delete_store(test_client):
    """
    Test Store 1 is deleted from DB
    """
    response = test_client.delete('/store/1')
    assert response.status_code == 200
    expected = {"message": "STORE_DELETED"}
    assert expected == json.loads(response.get_data(as_text=True))


def test_delete_store_not_found(test_client):
    """
    Test deletion of a Store that doesn't exist
    """
    response = test_client.delete('/store/1')
    assert response.status_code == 404
    expected = {"message": "STORE_NOT_FOUND"}
    assert expected == json.loads(response.get_data(as_text=True))


