from ..database import db

association_table_1 = db.Table('person_x_production', db.Model.metadata,
                               db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
                               db.Column('production_id', db.Integer, db.ForeignKey('production.id')),
                               )

association_table_2 = db.Table('used_tools_x_production', db.Model.metadata,
                               db.Column('resource_id', db.Integer, db.ForeignKey('resource.id')),
                               db.Column('production_id', db.Integer, db.ForeignKey('production.id')),
                               )

association_table_3 = db.Table('used_resources_x_production', db.Model.metadata,
                               db.Column('resource_id', db.Integer, db.ForeignKey('resource.id')),
                               db.Column('production_id', db.Integer, db.ForeignKey('production.id')),
                               )


class ProductionEntity(db.Model):
    __tablename__ = 'production'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    producers = db.relationship('PersonEntity', secondary=association_table_1, lazy='dynamic')
    used_tools = db.relationship('ResourceEntity', secondary=association_table_2, lazy='dynamic')
    used_resources = db.relationship('ResourceEntity', secondary=association_table_3, lazy='dynamic')
    building_room_id = db.Column(db.Integer, db.ForeignKey('building_room.id'))
    produced_in = db.relationship('BuildingRoomEntity', backref='productions')
