import pickle, os
from uuid import uuid1
from flask import Flask, request, render_template
from base64 import b64encode, b64decode

from flask.wrappers import Response


app = Flask(__name__)

class getuserid:
    def __init__(self, uuid=None):
        self.uuid = str(uuid1())


def __str__(self):
        return self.uuid

@app.route('/')
def index():
    user_obj = request.cookies.get('uuid')
    if user_obj == None:
            user_obj = getuserid()
            Response.set_cookie('uuid', b64encode(pickle.dumps(user_obj)))
            return render_template('index.html', the_title='Pickle Rick Home Page')
    else:
            pickle.loads(b64decode(user_obj))
            return render_template('index.html', the_title='Pickle Rick Home Page')

@app.route('/robots.txt')
def robots():
    return render_template('robots.txt', the_title='robots.txt')

@app.route('/flag.txt')
def flag():
    return render_template('flag.txt', the_title='flag.txt')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

