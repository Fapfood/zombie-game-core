from ..base_dao import BaseDAO
from ..entity import BuildingTypeEntity


class BuildingTypeDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, BuildingTypeEntity)
