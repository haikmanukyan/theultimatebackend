import flask
from flask import Flask
app = Flask(__name__, template_folder='flask/templates', static_folder='flask/assets')

class Page1:
    def __str__(self):
        return flask.render_template('index.html')


class Page2:
    def __init__(self):
        self.num_items = 10
    def __str__(self):
        items = ""
        for i in range(self.num_items):
            items += flask.render_template('item.html')

@app.route('/')
def hello_world():
    return str(Page1())