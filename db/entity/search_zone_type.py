from ..database import db


class SearchZoneTypeEntity(db.Model):
    __tablename__ = 'search_zone_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # search_rooms = db.relationship('ResourceDropProbabilityEntity', secondary=association_table_1)
