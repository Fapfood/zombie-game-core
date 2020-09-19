from ..database import db


class BuildingRoomEntity(db.Model):
    __tablename__ = 'building_room'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    production_type = db.Column(db.String)
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'))
    part_of = db.relationship('BuildingEntity', backref='rooms',
                              primaryjoin='BuildingRoomEntity.building_id==BuildingEntity.id')
