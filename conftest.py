import pytest
import app 
from controllers import movies


@pytest.fixture
def api(monkeypatch):
    test_movies = [
        {"id": 1, "movie_name": "Dune", "release_date": 2021, "director": "Denis Villeneuve"},
        {"id": 2, "movie_name": "Tenet", "release_date": 2020, "director": "Christopher Nolan"}
    ]
    monkeypatch.setattr(movies, "movies", test_movies)
    api = app.app.test_client()
    return api
