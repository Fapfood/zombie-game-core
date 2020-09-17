from ..database import db


class SkillEntity(db.Model):
    __tablename__ = 'skill'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    level = db.Column(db.Integer, nullable=False)

    def __le__(self, other):
        if self.type != other.type:
            return False
        if self.level <= other.level:
            return True
        return False

    def __lt__(self, other):
        if self.type != other.type:
            return False
        if self.level < other.level:
            return True
        return False

    def __ge__(self, other):
        if self.type != other.type:
            return False
        if self.level >= other.level:
            return True
        return False

    def __gt__(self, other):
        if self.type != other.type:
            return False
        if self.level > other.level:
            return True
        return False
