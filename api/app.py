from flask import Flask, request, jsonify
from werkzeug import exceptions 
from flask_cors import CORS
import user 


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/users', methods = ['GET', 'POST'])
def giriffle_handler():
    if request.method == 'GET':
        return jsonify(user.User.all())
    elif request.method == 'POST':
        data = request.json
        user.User
        return 'your information has been added', 201
  
@app.route('/user/<int:user>')
def indexed_user(user_id):
    return f"your username is  {user_id}"

@app.errorhandler(exceptions.NotFound)
def error_404(err):
    return jsonify({"message": f"Your giriffle has experiencing technical issues: {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"message": "It's your giriffle, not you"}), 500

if __name__ == ('__main__'):
    app.run(debug=True)