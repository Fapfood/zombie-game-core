from ..database import db

association_table = db.Table('skill_x_person', db.Model.metadata,
                             db.Column('skill_id', db.Integer, db.ForeignKey('skill.id')),
                             db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
                             )


class PersonEntity(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    base_icon = db.Column(db.String(1), nullable=False)
    temp_icon = db.Column(db.String(1))
    owned = db.Column(db.Boolean, nullable=False, default=False)
    attitude = db.Column(db.Integer, nullable=False)
    long = db.Column(db.Float, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    skills = db.relationship('SkillEntity', secondary=association_table)
    building_room_id = db.Column(db.Integer, db.ForeignKey('building_room.id'))
    assigned_to = db.relationship('BuildingRoomEntity', backref='workers')
