from ..database import db


class ZoneTypeEntity(db.Model):
    __tablename__ = 'zone_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # zone_rooms = db.relationship('ResourceDropProbabilityEntity', secondary=association_table_1)
