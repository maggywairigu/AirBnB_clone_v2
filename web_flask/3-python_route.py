#!/usr/bin/python3
"""
Routes:
/: Hello
/hbnb:
/c/<text>: , followed by the value of the text variable
(replace underscore _ symbols with a space )
/python/<text>: , followed by the value of the text variable
(replace underscore _ symbols with a space )
The default value of text is coolis
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "Python {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
