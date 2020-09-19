from ..base_dao import BaseDAO
from ..entity import BuildingRoomEntity


class BuildingRoomDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, BuildingRoomEntity)

    def read_all_by_building_id(self, id):
        objs = self.db.session.query(self.class_entity).filter_by(building_id=id).all()
        return objs
