import logging
from datetime import datetime
from sqlalchemy import orm

from app import db


class StandardMixin:
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(f"{self.__class__.__name__}(id={self.id})")
        super().__init__(*args, **kwargs)

    @orm.reconstructor
    def init_on_load(self):
        self.logger = logging.getLogger(f"{self.__class__.__name__}(id={self.id})")

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"
