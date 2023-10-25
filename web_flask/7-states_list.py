#!/usr/bin/python3
"""a script that starts a Flask web application and
handles @app.teardown_appcontext
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Teardown
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def html():
    """Displays html

    Returns:
        html
    """
    states = storage.all(State)
    value_dict = {i.id: i.name for i in states.values()}
    return render_template('7-states_list.html',
                           Table="States", items=value_dict)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
