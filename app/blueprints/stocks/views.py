from flask import render_template

from . import stocks


@stocks.route("/overview")
def overview():
    return render_template("stocks/overview.html")


@stocks.route("/uk_market")
def uk_market():
    return render_template("stocks/uk_market.html")


@stocks.route("/uk_screener")
def uk_screener():
    return render_template("stocks/uk_screener.html")


@stocks.route("/us_market")
def us_market():
    return render_template("stocks/us_market.html")


@stocks.route("/us_screener")
def us_screener():
    return render_template("stocks/us_screener.html")
