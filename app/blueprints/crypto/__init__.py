from flask import Blueprint

crypto = Blueprint("crypto", __name__)

from . import views