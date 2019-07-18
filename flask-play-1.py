#
# Example  setup if needed 
#  export FLASK_ENV=development
#  export FLASK_APP=app.py
#


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Server Is Up   !'


@app.route('/greet')
def say_hello():
    return 'Greet API Called'

if __name__ == '__main__':
    app.run()
