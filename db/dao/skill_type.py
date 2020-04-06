from ..base_dao import BaseDAO
from ..entity import SkillTypeEntity


class SkillTypeDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, SkillTypeEntity)
