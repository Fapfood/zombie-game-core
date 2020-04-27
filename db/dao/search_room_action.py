from ..base_dao import BaseDAO
from ..entity import SearchRoomActionEntity


class SearchRoomActionDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, SearchRoomActionEntity)
