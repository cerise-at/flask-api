from flask import Flask, request, jsonify
from werkzeug import exceptions
from flask_cors import CORS
from controllers import movies

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return jsonify({"message": "Welcome to the movies API!"}), 200

@app.route('/movies', methods = ['GET', 'POST'])
def movie_handler():

    if request.method == 'GET':
        return jsonify(movies.all()), 200

    elif request.method == 'POST':
        movie = movies.create(request)
        return movie

@app.route('/users/<int:user_id>', methods=['GET', 'DELETE'])
def indexed_user(user_id):

    if request.method == 'GET':
        user = users.find_by_id(user_id)
        return user

    elif request.method == 'DELETE':
        user = users.destroy(user_id)
        return user
        
@app.errorhandler(exceptions.NotFound)
def error_404(err):
    return jsonify({"message": f"Not Found: {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def error_500(err):
    return jsonify({"message": "Internal Server Error"}), 500

if __name__ == ('__main__'):
    app.run(debug=True)
