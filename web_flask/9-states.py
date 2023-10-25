#!/usr/bin/python3
"""a script that starts a Flask web application and
handles @app.teardown_appcontext
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Teardown to remove the current SQLAlchemy Session
    """
    storage.close()


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def html_display(id=None):
    """Displays html page

    Returns:
        html
    """
    states = storage.all(State)
    if not id:
        html_dict = {value.id: value.name for value in states.values()}
        return render_template('7-states_list.html',
                               Table="States",
                               items=html_dict)

    k = "State.{}".format(id)
    if k in states:
        return render_template('9-states.html',
                               Table="State: {}".format(states[k].name),
                               items=states[k])

    return render_template('9-states.html',
                           items=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
