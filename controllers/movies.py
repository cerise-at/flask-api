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
    movie = [movie for movie in movies if movie['id'] == id]
    # user = [users.filter(lambda users['id'] == id)]
    print(movie)
