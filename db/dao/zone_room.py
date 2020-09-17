from ..base_dao import BaseDAO
from ..entity import ZoneRoomEntity


class ZoneRoomDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, ZoneRoomEntity)
