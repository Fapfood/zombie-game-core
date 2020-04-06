from ..database import db


class SkillTypeEntity(db.Model):
    __tablename__ = 'skill_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
