import json

def test_index(app, client):
    del app
    ans = client.get('/welcome')
    assert ans.status_code == 200
    expected = {'message': 'Welcome to Pizza House'}
    assert json.loads(ans.data) == expected

def test_accept_order(app, client):
    del app
    ans = client.post('/order', json={'order': ['Pizza1', 'Pizza2']})
    assert ans.status_code == 200
    if ans.status_code == 200:
        assert json.loads(ans.data)['order_id'] is not None


def test_getorders(app, client):
    del app
    ans = client.get('/getorders')
    j = json.loads(ans.data)
    assert ans.status_code == 200
    expected = 200
    assert ans.status_code == expected

def test_getorder(app, client):
    del app
    ans = client.get('/getorders/6346a977d32250a2d45a1a2b')
    j = json.loads(ans.data)
    assert ans.status_code == 404
    expected = 404
    assert ans.status_code == expected