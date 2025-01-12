# import flast module
from flask import Flask,jsonify,request,abort
from flask_cors import CORS

# instance of flask application
app = Flask(__name__)
CORS(app)

# home route that returns below text when root url is accessed
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/save",methods=["POST"])
def save():
    requiredParms = ["cardID","regularQuantity","reverseQuantity","firstEditionQuantity","shadowlessQuantity"]
    body = request.form.to_dict() 
    missingParams = [x for x in requiredParms if x not in body.keys()]
    if (len(missingParams) > 0):
        abort(400, "Missing the following parameter: "+','.join(missingParams)) 
    
    data = {'key': 'vaaaalue'}
    return jsonify(data)

if __name__ == '__main__':  
   app.run()  
