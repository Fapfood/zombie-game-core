from ..base_dao import BaseDAO
from ..entity import SearchRoomBlankEntity


class SearchRoomBlankDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, SearchRoomBlankEntity)
