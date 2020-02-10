def test_basic(client):
    res = client.get('keep/')

    assert res.status_code == 200
