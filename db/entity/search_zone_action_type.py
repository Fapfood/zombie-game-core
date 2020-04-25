from ..database import db


class SearchZoneActionTypeEntity(db.Model):
    __tablename__ = 'search_zone_action_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    probability = db.Column(db.Float, nullable=False)
