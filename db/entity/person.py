from ..database import db

association_table = db.Table('skill_level_x_person', db.Model.metadata,
                             db.Column('skill_level_id', db.Integer, db.ForeignKey('skill_level.id')),
                             db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
                             )


class PersonEntity(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    owned_skills = db.relationship('SkillLevelEntity', secondary=association_table)
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'))
    assigned_to = db.relationship('BuildingEntity', backref='workers')
