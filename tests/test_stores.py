import json


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
	"description": "This is store 1",
    }
    res = test_client.post('/store', data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert res.status_code == 201
    expected = {'message': 'STORE_CREATED'}
    assert expected == json.loads(res.get_data(as_text=True))


def test_patch_store_succeeds(test_client):
    mock_request_headers = {
        'Content-Type': 'application/json'
    }
    mock_request_data = {
   	"name": "store 1A",
	"description": "This is store 1A",
    }
    res = test_client.patch('/store/1', data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert res.status_code == 200
    expected = {
        "id": 1,
        "name": "store 1A",
        "description": "This is store 1A"
    }
    assert expected == json.loads(res.get_data(as_text=True))


def test_patch_store_not_found(test_client):
    mock_request_headers = {
        'Content-Type': 'application/json'
    }
    mock_request_data = {
   	"name": "store 1A",
	"description": "This is store 1A",
    }
    res = test_client.patch('/store/2', data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert res.status_code == 404
    expected = {'message': 'STORE_NOT_FOUND'}
    assert expected == json.loads(res.get_data(as_text=True))


