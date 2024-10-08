#!/usr/bin/env python3
""" Module for basic babel config"""

import babel
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Function for rendering template """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
