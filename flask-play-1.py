#
#  various examples
#  Example  setup if needed
#  export FLASK_ENV=development
#  export FLASK_APP=app.py
#

import json

from flask import Flask
from flask import Response
from flask import jsonify



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Server Is Up   !'


@app.route('/greet')
def say_hello():
    return 'Greet API Called'


@app.route("/json1")
def route1():
    dict1 = {"prop1": "p1", "prop2": "p2"}
    return Response(json.dumps(dict1), mimetype='application/json')


@app.route("/json2")
def route2():
    return jsonify({'data':{"prop1": "p1", "prop2": "p2"}})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

