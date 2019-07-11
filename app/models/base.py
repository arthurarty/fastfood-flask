import sqlalchemy as sa
from flask_sqlalchemy import Model


class BaseModel(Model):
    """Base class for models"""
    id = sa.Column(sa.Integer, primary_key=True)

    def add_to_session(self, db_session):
        """Add to session and commit"""
        db_session.session.add(self)
        db_session.session.commit()

    @classmethod
    def find(cls, id=None, unique_field=None):
        """Find item by id or unique_field provided as string"""
        if id is None:
            return cls.query.filter(
                (id == id) | (unique_field == unique_field)).first()
        return cls.query.filter_by(id=id).first()
