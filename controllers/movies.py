movies = [
{"id": 1, "movie_name": "Dune", "release_date": 2021, "director": "Denis Villeneuve"}
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
