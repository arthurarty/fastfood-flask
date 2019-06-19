from app import db


class User(db.Model):
    """User model creates user given a password and email."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    admin = db.Column(db.Boolean(), nullable=False, default=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def find(id=None, email=None):
        """Find user by id or email"""
        return User.query.filter((id == id) | (email == email)).first()
