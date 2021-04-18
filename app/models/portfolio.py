
from app import db

from .common import StandardMixin


class Portfolio(StandardMixin, db.Model):
	__tablename__ = "portfolios"
	name = db.Column(db.String(64))

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	assets = db.relationship("Asset", backref="portfolio")

	def calc_cost(self):
		return sum([asset.cost * asset.volume for asset in self.assets])