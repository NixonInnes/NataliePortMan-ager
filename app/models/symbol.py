from app import db

from .common import StandardMixin


class Symbol(StandardMixin, db.Model):
    __tablename__ = "symbols"
    name = db.Column(db.String(32))
    ticker = db.Column(db.String(12), unique=True, index=True)
    is_crypto = db.Column(db.Boolean, default=False)

    assets = db.relationship("Asset", backref="symbol")
