import json

def test_welcome(api):
    res = api.get('/')
    assert res.status == '200 OK'
    assert res.json['message'] == "Welcome to the movies API!"

def test_get_movies(api):
    res = api.get('/movies/')
    assert res.status == '200 OK'
    assert len(res.json) == 2

def test_get_movie_by_id(api):
    res = api.get('/movies/1')
    assert res.status == '200 OK'
    assert res.json['movie_name'] == 'Dune'

def test_get_movies_error(api):
    res = api.get('/movies/10/')
    assert res.status == '404 NOT FOUND'
    assert "Not Found" in res.json['message']

def test_post_movies(api):
    mock_data = json.dumps({"id": 3, "movie_name": "The King", "release_date": 2019, "director": "David Michôd"})
    mock_headers = {'Content-Type': 'application/json'}
    res = api.post('/movies/', data=mock_data, headers=mock_headers)
    assert res.json['id'] == 3

def test_not_found(api):
    res = api.get('/non/')
    assert res.status == '404 NOT FOUND'
    assert 'Not Found' in res.json['message']
