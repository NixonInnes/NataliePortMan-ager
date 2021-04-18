from datetime import datetime

from app import db

from .common import StandardMixin


class Transaction(StandardMixin, db.Model):
    __tablename__ = "transactions"

    buy = db.Column(db.Boolean, default=True)
    volume = db.Column(db.Float)
    price = db.Column(db.Float)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    asset_id = db.Column(db.Integer, db.ForeignKey("assets.id"))
