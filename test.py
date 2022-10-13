import json

def _welcome(app, client):
    del app
    ans = client.get('/welcome')
    expected = {'message': 'Welcome to Pizza House'}
    assert json.loads(ans.data) == expected

def _accept_order(app, client):
    del app
    ans = client.post('/order', json={'order': ['Pizza1', 'Pizza2']})
    if ans.status_code == 200:
        assert json.loads(ans.data)['order_id'] is not None


def _getorders(app, client):
    del app
    ans = client.get('/getorders')
    j = json.loads(ans.data)
    

def _getorder(app, client):
    del app
    ans = client.get('/getorders/6346a977d32250a2d45a1a2b')
    j = json.loads(ans.data)
    
