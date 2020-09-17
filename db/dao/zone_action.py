from ..base_dao import BaseDAO
from ..entity import ZoneActionEntity


class ZoneActionDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, ZoneActionEntity)
