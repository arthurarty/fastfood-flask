from app import db
from .menu import Menu
from psycopg2 import IntegrityError
from .time_stamp_mixin import TimestampMixin


class Order(TimestampMixin, db.Model):
    """Orders created by customers"""

    __tablename__ = 'orders'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'))
    menu = db.relationship('Menu', backref=db.backref('orders', lazy=True))
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(), nullable=False)

    def __init__(self, quantity):
        self.quantity = quantity
        self.status = 'New'

    def __repr__(self):
        return '<OrderItem %r>' % self.id

    def save(self, user, menu_id):
        """Db session add and commit"""
        user.orders.append(self)
        menu_item = Menu.find(menu_id)
        if menu_item is None:
            raise IntegrityError
        menu_item.orders.append(self)
        return self.add_to_session(db)
