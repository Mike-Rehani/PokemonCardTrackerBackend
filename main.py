# import flast module
from flask import Flask,jsonify
from flask_cors import CORS

# instance of flask application
app = Flask(__name__)
CORS(app)

# home route that returns below text when root url is accessed
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test")
def test():
    data = {'key': 'value'}
    return jsonify(data)

if __name__ == '__main__':  
   app.run()  
