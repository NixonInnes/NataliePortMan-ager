from flask import Blueprint

stocks = Blueprint("stocks", __name__)

from . import views