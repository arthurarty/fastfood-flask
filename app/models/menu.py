from app import db
from .time_stamp_mixin import TimestampMixin


class Menu(TimestampMixin, db.Model):
    """Model for menu items"""

    __tablename__ = 'menus'

    name = db.Column(db.String(255), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<MenuItem %r>' % self.name

    def __init__(self, name=None, price=None, description=None):
        self.name = name
        self.price = price
        self.description = description

    def save(self):
        """Save menu_item to db."""
        return self.add_to_session(db)
