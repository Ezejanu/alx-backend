#!/usr/bin/env python3
"""Basic Flask App"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', page_title='Welcome to Holberton',
                           header='Hello world')


if __name__ == '__main__':
    app.run(debug=True)
