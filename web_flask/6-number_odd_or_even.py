#!/usr/bin/python3


"""utilizing Flask for Web app frame work"""
from flask import Flask, escape, render_template

app = Flask(__name__)



@app.route("/", strict_slashes = False)
def home():
    """method that defines '/' route for Flask web application"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes = False)
def hbnb():
    """method that defines '/hbnb' route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes = False)
def show_text(text):
    """method that defines '/c/' route that uses a variable"""
    return 'C %s' % escape(text)


@app.route('/python/', strict_slashes = False)
@app.route('/python/<text>', strict_slashes = False)
def show_text2(text="is cool"):
    """method that defines '/python/' route that uses a variable"""
    return 'Python %s' % escape(text)


@app.route('/number/<int:n>', strict_slashes = False)
def show_text3(n):
    """method that defines '/number/' route that uses a variable"""
    if isinstance(n, int):
        return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes = False)
def show_text4(n):
    """method that defines '/number_template/' route that uses a variable"""
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes = False)
def show_text5(n):
    """
    method that defines '//number_odd_or_even/' route that uses a variable
    """
    if n % 2 == 0:
        num_string = "Number: {} is even".format(n)

    elif n % 2 != 0:
        num_string = "Number: {} is odd".format(n)

    return render_template('6-number_odd_or_even.html', num_string=num_string)

if __name__ == "__main__":
    app.run(host="localhost")
