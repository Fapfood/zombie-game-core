from ..database import db


class SearchZoneEntity(db.Model):
    __tablename__ = 'search_zone'
    id = db.Column(db.Integer, primary_key=True)
