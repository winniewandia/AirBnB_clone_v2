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
    """Teardown to remove the current SQLAlchemy Session
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def html_display():
    """Displays html page

    Returns:
        html
    """
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html',
                           states=states_sorted)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
