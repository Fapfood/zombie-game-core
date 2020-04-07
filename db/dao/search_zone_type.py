from ..base_dao import BaseDAO
from ..entity import SearchZoneTypeEntity


class SearchZoneTypeDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, SearchZoneTypeEntity)
