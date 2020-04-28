from ..database import db


class SearchRoomActionEntity(db.Model):
    __tablename__ = 'search_room_action'
    id = db.Column(db.Integer, primary_key=True)
