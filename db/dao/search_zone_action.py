from ..base_dao import BaseDAO
from ..entity import SearchZoneActionEntity


class SearchZoneActionDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, SearchZoneActionEntity)
