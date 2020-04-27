from ..base_dao import BaseDAO
from ..entity import ShapeMultiPolygonEntity
from ..entity import ShapePointEntity
from ..entity import ShapePolygonEntity
from ..entity import ShapeRingEntity


class ShapePointDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, ShapePointEntity)


class ShapeRingDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, ShapeRingEntity)


class ShapePolygonDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, ShapePolygonEntity)


class ShapeMultiPolygonDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, ShapeMultiPolygonEntity)
