from ..base_dao import BaseDAO
from ..entity import SkillLevelEntity


class SkillLevelDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, SkillLevelEntity)

    def read_by_type_id_and_level(self, type_id, level):
        obj = self.db.session.query(self.class_entity).filter_by(skill_type_id=type_id, level=level).one_or_none()
        return obj

    def read_all_by_type_name(self, id):
        # obj = self.db.session.query(self.class_entity).join(ResourceTypeEntity).filter(
        #     ResourceTypeEntity.id == id).all()
        obj = self.db.session.query(self.class_entity).filter_by(resource_type_id=id).all()
        return obj
