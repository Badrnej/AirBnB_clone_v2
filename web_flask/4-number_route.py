#!/usr/bin/python3
"""
hello Flask web app!
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    HBNB !
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def widlcard(text):
    """
    Widlcard usage :)
    """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def widlcard_two(text):
    """
    Wildcard second :)
    """
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:num>", strict_slashes=False)
def number_route(num):
    """
    number wildcard :)
    """
    return f"{num} is a number"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
