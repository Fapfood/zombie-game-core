from ..base_dao import BaseDAO
from ..entity import ProductionEntity


class ProductionDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, ProductionEntity)
