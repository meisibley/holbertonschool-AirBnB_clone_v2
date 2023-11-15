#!/usr/bin/python3
'''display a HTML page for a states and amenities and their contains'''
from models import storage
from flask import Flask, render_template
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def display_hbnb():
    '''display hbnb filters storage to a HTML page'''
    states = storage.all('State').values()
    cities = storage.all('City').values()
    amenities = storage.all('Amenity').values()
    return render_template("10-hbnb_filters.html", cities=cities,
                           states=states, amenities=amenities)


@app.teardown_appcontext
def close_session(exc):
    '''close the SQLAlchemy session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)