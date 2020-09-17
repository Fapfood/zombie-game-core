from ..base_dao import BaseDAO
from ..entity import ZoneRoomActionEntity


class ZoneRoomActionDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, ZoneRoomActionEntity)
