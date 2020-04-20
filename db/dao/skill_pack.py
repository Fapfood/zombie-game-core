from ..base_dao import BaseDAO
from ..entity import SkillPackEntity


class SkillPackDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, SkillPackEntity)

    def read_by_name(self, name):
        obj = self.db.session.query(self.class_entity).filter_by(name=name).one_or_none()
        return obj
