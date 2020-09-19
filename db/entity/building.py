from ..database import db


class BuildingEntity(db.Model):
    __tablename__ = 'building'
    id = db.Column(db.Integer, primary_key=True)
    building_room_id = db.Column(db.Integer, db.ForeignKey('building_room.id'))
    focused_on = db.relationship('BuildingRoomEntity',
                                 primaryjoin='BuildingEntity.building_room_id==BuildingRoomEntity.id',
                                 post_update=True)
    multipolygon_id = db.Column(db.Integer, db.ForeignKey('shape_multipolygon.id'), nullable=False)
    shape = db.relationship('ShapeMultiPolygonEntity')
