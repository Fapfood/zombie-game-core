from ..database import db


class SearchZoneActionEntity(db.Model):
    __tablename__ = 'search_zone_action'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    required_number_of_people = db.Column(db.Integer, nullable=False)
    # required_skills = db.relationship('SkillLevelEntity', secondary=None)
    # required_resources = db.relationship('ResourcePackEntity', secondary=None)
