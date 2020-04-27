from ..base_dao import BaseDAO
from ..entity import SearchRoomEntity


class SearchRoomDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, SearchRoomEntity)
