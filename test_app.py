import json

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == "Welcome to the movies API!"

    def test_get_movies(self, api):
        res = api.get('/api/movies')
        assert res.status == '200 OK'
        assert len(res.json) == 1

    def test_get_movie_by_id(self, api):
        res = api.get('/api/movies/1')
        assert res.status == '200 OK'
        assert res.json['movie_name'] == 'Dune'

    def test_get_movies_error(self, api):
        res = api.get('/api/movies/10')
        assert res.status == '400 BAD REQUEST'
        assert "movie with id 10" in res.json['message']

    def test_post_movies(self, api):
        mock_data = json.dumps({'movie_name': 'Tenet'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/api/movies', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 2

    def test_not_found(self, api):
        res = api.get('/non')
        assert res.status == '404 NOT FOUND'
        assert 'Oops!' in res.json['message']
