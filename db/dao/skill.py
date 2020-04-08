from ..base_dao import BaseDAO
from ..entity import SkillEntity


class SkillDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, SkillEntity)
