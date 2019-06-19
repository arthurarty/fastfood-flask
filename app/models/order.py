from app import db
from .user import User
from .menu import Menu
from psycopg2 import IntegrityError


class Order(db.Model):
    """Orders created by customers"""

    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'))
    menu = db.relationship('Menu', backref=db.backref('orders', lazy=True))
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, quantity):
        self.quantity = quantity
        self.status = 'New'

    def __repr__(self):
        return '<OrderItem %r>' % self.id

    def save(self, user_id, menu_id):
        """Db session add and commit"""
        user = User.find(user_id)
        user.orders.append(self)
        menu_item = Menu.find(menu_id)
        if menu_item is None:
            raise IntegrityError
        menu_item.orders.append(self)
        db.session.add(self)
        db.session.commit()
