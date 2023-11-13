#!/usr/bin/python3
'''using Flask to display HBNB data, list states'''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def cls_session(self):
    '''close current SQLAlchemy session'''
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list():
    '''using HTML page to display states list'''
    st_list = []
    for st in storage.all(State).values():
        st_list.append((st.name, st.id))
        st_list.sort(key=lambda items: items[0])
    return renden_template("7-states_list.html", states_list=st_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
