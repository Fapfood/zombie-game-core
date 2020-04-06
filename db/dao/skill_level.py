from ..base_dao import BaseDAO
from ..entity import SkillLevelEntity


class SkillLevelDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, SkillLevelEntity)
