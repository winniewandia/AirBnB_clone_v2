#!/usr/bin/python3
"""A script that starts a Flask web application and has 3 routes
"""
from markupsafe import escape
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """function to display hello HBNB

    Returns:
        web application
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function to display HBNB"
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """display “C ” followed by the value of the text variable

    Args:
        text (str): user input

    Returns:
        web application
    """
    return f'C {escape(text)}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
