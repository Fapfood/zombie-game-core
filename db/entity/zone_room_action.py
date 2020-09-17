from ..database import db


class ZoneRoomActionEntity(db.Model):
    __tablename__ = 'zone_room_action'
    id = db.Column(db.Integer, primary_key=True)
