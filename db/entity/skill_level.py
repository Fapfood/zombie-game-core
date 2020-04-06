from ..database import db


class SkillLevelEntity(db.Model):
    __tablename__ = 'skill_level'
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer, nullable=False)
    skill_type_id = db.Column(db.Integer, db.ForeignKey('skill_type.id'))
    type = db.relationship('SkillTypeEntity')

    def __le__(self, other):
        if self.skill_type_id != other.skill_type_id:
            return False
        if self.level <= other.level:
            return True
        return False

    def __lt__(self, other):
        if self.skill_type_id != other.skill_type_id:
            return False
        if self.level < other.level:
            return True
        return False

    def __ge__(self, other):
        if self.skill_type_id != other.skill_type_id:
            return False
        if self.level >= other.level:
            return True
        return False

    def __gt__(self, other):
        if self.skill_type_id != other.skill_type_id:
            return False
        if self.level > other.level:
            return True
        return False
