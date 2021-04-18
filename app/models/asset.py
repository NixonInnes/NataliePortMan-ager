from datetime import datetime

from app import db

from .common import StandardMixin


class Asset(StandardMixin, db.Model):
	__tablename__ = "assets"
	bought_on = db.Column(db.DateTime, default=datetime.utcnow)
	volume = db.Column(db.Float)
	price = db.Column(db.Float)

	symbol_id = db.Column(db.Integer, db.ForeignKey("symbols.id"))
	user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
	portfolio_id = db.Column(db.Integer, db.ForeignKey("portfolios.id"))