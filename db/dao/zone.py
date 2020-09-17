from ..base_dao import BaseDAO
from ..entity import ZoneEntity


class ZoneDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, ZoneEntity)
