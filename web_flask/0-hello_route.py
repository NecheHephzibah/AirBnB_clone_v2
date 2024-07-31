#!/usr/bin/python3
<<<<<<< HEAD
"""a script that starts a flask web application"""
=======
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
>>>>>>> f10c55ce1b1b78ff7518aaa0beb07a7450ae3bc5
from flask import Flask

app = Flask(__name__)


<<<<<<< HEAD
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ a function that prints hello `hbnb at the root"""
=======
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
>>>>>>> f10c55ce1b1b78ff7518aaa0beb07a7450ae3bc5
    return "Hello HBNB!"


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=5000)
=======
    app.run(host="0.0.0.0")
>>>>>>> f10c55ce1b1b78ff7518aaa0beb07a7450ae3bc5
