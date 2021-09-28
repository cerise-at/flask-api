from flask import Flask, request, jsonify
from werkzeug import exceptions 
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/users', methods = ['GET', 'POST'])
def giriffle_handler():
    if request.method == 'GET':
        return jsonify(User.query.all())
    elif request.method == 'POST':
        data = request.json
        db.session.add(data['username'])
        db.session.add(data['age'])
        db.session.add(data['height'])
        db.session.commit()
        return 'your information has been added', 201
  
@app.route('/giriffle/<int:giriffle_id>')
def indexed_giriffle(giriffle_id):
    return f"Thank you for purchasing your giriffle. Your personal giriffle has the id {giriffle_id}"

@app.errorhandler(exceptions.NotFound)
def error_404(err):
    return jsonify({"message": f"Your giriffle has experiencing technical issues: {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"message": "It's your giriffle, not you"}), 500

if __name__ == ('__main__'):
    app.run(debug=True)