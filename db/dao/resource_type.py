from ..base_dao import BaseDAO
from ..entity import ResourceTypeEntity


class ResourceTypeDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, ResourceTypeEntity)
