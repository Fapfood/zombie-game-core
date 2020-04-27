from ..base_dao import BaseDAO
from ..entity import SkillLevelEntity
from ..entity import SkillTypeEntity


class SkillLevelDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, SkillLevelEntity)

    def read_by_name(self, name):
        obj = self.db.session.query(self.class_entity).filter_by(name=name).one_or_none()
        return obj

    def read_by_type_id_and_level(self, type_id, level):
        obj = self.db.session.query(self.class_entity).filter_by(skill_type_id=type_id, level=level).one_or_none()
        return obj

    def read_by_type_name_and_level(self, type_name, level):
        obj = self.db.session.query(self.class_entity).join(SkillTypeEntity).filter(
            SkillTypeEntity.name == type_name, self.class_entity.level == level).one_or_none()
        return obj
