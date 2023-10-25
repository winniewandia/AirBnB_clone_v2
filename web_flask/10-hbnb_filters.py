#!/usr/bin/python3
"""a script that starts a Flask web application and
handles @app.teardown_appcontext
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Teardown to remove the current SQLAlchemy Session
    """
    storage.close()


@app.route('/hbnb_filters/', strict_slashes=False)
def html_display():
    """Displays html page

    Returns:
        html
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=states.values(), amenities=amenities.values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
