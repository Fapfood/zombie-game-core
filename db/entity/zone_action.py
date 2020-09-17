from ..database import db


class ZoneActionEntity(db.Model):
    __tablename__ = 'zone_action'
    id = db.Column(db.Integer, primary_key=True)
