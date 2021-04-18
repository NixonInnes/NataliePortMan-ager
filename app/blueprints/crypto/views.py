from flask import render_template

from . import crypto


@crypto.route("/screener")
def screener():
	return render_template("crypto/screener.html")