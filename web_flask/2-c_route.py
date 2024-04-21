#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """Displays 'Hello HBNB!' message"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Displays 'HBNB' message"""
    return "HBNB"


@app.route("/c/<text>")
def c_route(text):
    """Displays 'C ' followed by the text variable with spaces replacing underscores"""
    return f"C {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

