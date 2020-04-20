from ..database import db

association_table = db.Table('skill_level_x_skill_pack', db.Model.metadata,
                             db.Column('skill_level_id', db.Integer, db.ForeignKey('skill_level.id')),
                             db.Column('skill_pack_id', db.Integer, db.ForeignKey('skill_pack.id')),
                             )


class SkillPackEntity(db.Model):
    __tablename__ = 'skill_pack'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    skills = db.relationship('SkillLevelEntity', secondary=association_table)
