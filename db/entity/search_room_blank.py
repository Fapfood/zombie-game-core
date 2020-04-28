from ..database import db


class SearchRoomBlankEntity(db.Model):
    __tablename__ = 'search_room_blank'
    id = db.Column(db.Integer, primary_key=True)
