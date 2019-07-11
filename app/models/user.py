from app import db
from .time_stamp_mixin import TimestampMixin


class User(TimestampMixin, db.Model):
    """User model creates user given a password and email."""

    __tablename__ = 'users'

    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    admin = db.Column(db.Boolean(), nullable=False, default=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def save(self):
        """Save user to db"""
        return self.add_to_session(db)
