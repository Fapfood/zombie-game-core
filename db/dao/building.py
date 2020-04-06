from ..base_dao import BaseDAO
from ..entity import BuildingEntity


class BuildingDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, BuildingEntity)
