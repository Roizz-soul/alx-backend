#!/usr/bin/env python3
""" Simple flask app """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/',  methods=['GET'], strict_slashes=False)
def index():
    """ First function """
    return render_templates('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
