from flask import Flask, request, jsonify
from werkzeug import exceptions
from flask_cors import CORS
from controllers import users

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return jsonify({"message": "welcome to the users API"}), 200

@app.route('/users', methods = ['GET', 'POST'])
def user_handler():

    if request.method == 'GET':
        return jsonify(users.all()), 200

    elif request.method == 'POST':
        user = users.create(request)
        return user

@app.route('/users/<int:user_id>')
def indexed_user(user_id):
    users.find_by_id(id)
    return ''

@app.errorhandler(exceptions.NotFound)
def error_404(err):
    return jsonify({"message": f"Not Found: {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"message": "Internal Server Error"}), 500

if __name__ == ('__main__'):
    app.run(debug=True)
