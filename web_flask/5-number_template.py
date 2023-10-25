#!/usr/bin/python3
"""A script that starts a Flask web application and has 6 routes
and renders a template
"""
from markupsafe import escape
from flask import Flask, render_template

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
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """function with default value of text

    Args:
        text (str): Defaults to 'is cool'.

    Returns:
        web application
    """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """returns only if n is an int

    Args:
        n (int): int to be returned

    Returns:
        web application
    """
    return f'{n} is a number'


# @app.route('/number_template/', strict_slashes=False)
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """route that displays HTML only if n is int

    Args:
        n (int): int to be displayed

    Returns:
        HTML: html page
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
