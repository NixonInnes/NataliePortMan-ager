from flask import render_template, redirect, request, url_for, current_app

from . import main


@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@main.route("/calendar", methods=["GET"])
def calendar():
    return render_template("calendar.html")


@main.route("/chart/<symbol>", methods=["GET"])
def chart(symbol):
    return render_template("chart.html", symbol=symbol)


@main.route("/info/<symbol>", methods=["GET"])
def info(symbol):
    return render_template("info.html", symbol=symbol)


@main.route("/_info", methods=["GET"])
def _info():
    symbol=request.args.get("tvwidgetsymbol", "AAPL")
    return render_template("info.html", symbol=symbol)
