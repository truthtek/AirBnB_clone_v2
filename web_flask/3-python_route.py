#!/usr/bin/python3

"""Flask Web Application"""

from flask import Flask, escape

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def home():
    """Route for the home page"""
    return "Hello HBNB!"

@app.route("/hbnb")
def hbnb():
    """Route for the HBNB page"""
    return "HBNB"

@app.route('/c/<text>')
def show_text(text):
    """Route for displaying text with replaced underscores"""
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/')
@app.route('/python/<text>')
def show_text2(text="is cool"):
    """Route for displaying Python text with replaced underscores"""
    return 'Python {}'.format(text.replace('_', ' '))

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 error handler"""
    return "Not Found", 404

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000)
    except KeyboardInterrupt:
        print("Server stopped")
