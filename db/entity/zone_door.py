from ..database import db


class ZoneDoorEntity(db.Model):
    __tablename__ = 'zone_door'
    id = db.Column(db.Integer, primary_key=True)
