import json

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == "Welcome to the movies API!"

    def test_all(self, api):
        res = api.get('/movies')
        assert res.status == '200 OK'
        assert len(res.json) == 1

    def test_find_by_id(self, api):
        res = api.get('/movies/1')
        assert res.status == '200 OK'
        assert res.json['movie_name'] == 'Terminator'

    def test_post_movies(self, api):
        mock_data = json.dumps({'movie_name': 'Stand by me'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/movies', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 2
    
    def test_put_movie(self, api):
        mock_data = json.dumps({'release_date': 2000})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.put('/movies/1', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 1
        assert res.json['release_date'] == 2000

    def test_delete_movie(self, api):
        res = api.delete('/movies/1')
        assert res.status == '204 NO CONTENT'

    def test_not_found(self, api):
        res = api.get('/non')
        assert res.status == '404 NOT FOUND'
        assert 'Not Found' in res.json['message']
