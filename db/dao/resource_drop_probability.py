from ..base_dao import BaseDAO
from ..entity import ResourceDropProbabilityEntity


class ResourceDropProbabilityDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, ResourceDropProbabilityEntity)
