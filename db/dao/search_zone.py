from ..base_dao import BaseDAO
from ..entity import SearchZoneEntity


class SearchZoneDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, SearchZoneEntity)
