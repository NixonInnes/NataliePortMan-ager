from flask import Blueprint

forex = Blueprint("forex", __name__)

from . import views
