from ..database import db


class ZoneEntity(db.Model):
    __tablename__ = 'zone'
    id = db.Column(db.Integer, primary_key=True)
