movies = [
{"id": 1, "movie_name": "Dune", "release_date": 2021, "director": "Denis Villeneuve"},
{"id": 2, "movie_name": "Tenet", "release_date": 2020, "director": "Christopher Nolan"},
{"id": 3, "movie_name": "A Quiet Place Part II", "release_date": 2020, "director": "John Krasinski"},
{"id": 4, "movie_name": "Wonder Woman 1984", "release_date": 2020, "director": "Patty Jenkins"},
{"id": 5, "movie_name": "The King", "release_date": 2019, "director": "David Michôd"}
]

def all():
    return [movie for movie in movies]

def create(data):
    movie = data.get_json()
    movie["id"] = len(movies) + 1
    movies.append(movie)
    return movie, 201

def find_by_id(id):
    movie = next(movie for movie in movies if movie['id'] == id)
    return movie

def destroy(id):
    movie = find_by_id(id)
    movies.remove(movie)
    return movie, 204
