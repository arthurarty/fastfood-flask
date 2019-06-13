from app import db


class Menu(db.Model):
    """User model creates user given a password and email."""

    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<MenuItem %r>' % self.name

    def save(self):
        db.session.add(self)
        db.session.commit()
