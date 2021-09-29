import pytest
import app 
from controllers import movies


@pytest.fixture
def api(monkeypatch):
    test_movies = [{'id': 1, 'movie_name': 'Terminator', 'release_date': 1984, 'director': 'James Cameron'}]
    monkeypatch.setattr(movies, "movies", test_movies)
    api = app.app.test_client()
    return api
