#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
=======
'''A simple Flask web application.
'''
from flask import Flask


app = Flask(__name__)
'''The Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''The home page.'''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
>>>>>>> 131f711afeb69783172c782ec160f5aa9bf663e4
