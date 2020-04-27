from ..database import db


class SearchRoomTypeEntity(db.Model):
    __tablename__ = 'search_room_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
