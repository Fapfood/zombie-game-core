from ..database import db


class SearchZoneActionEntity(db.Model):
    __tablename__ = 'search_zone_action'
    id = db.Column(db.Integer, primary_key=True)
