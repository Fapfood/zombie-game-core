from ..base_dao import BaseDAO
from ..entity import ResourcePackEntity


class ResourcePackDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, ResourcePackEntity)
