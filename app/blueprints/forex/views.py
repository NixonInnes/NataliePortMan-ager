from flask import render_template

from . import forex


@forex.route("/xchart")
def xchart():
    return render_template("forex/xchart.html")


@forex.route("/heatchart")
def heatchart():
    return render_template("forex/heatchart.html")


@forex.route("/screener")
def screener():
    return render_template("forex/screener.html")
