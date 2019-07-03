from app import db


class Menu(db.Model):
    """List of menu items avaliable"""

    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __repr__(self):
        return '<MenuItem %r>' % self.name

    def __init__(self, name=None, price=None, description=None):
        self.name = name
        self.price = price
        self.description = description

    def save(self):
        """Save menu_item to db."""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def find(id):
        """Find menu_item by id"""
        return Menu.query.filter_by(id=id).first()
