from ..base_dao import BaseDAO
from ..entity import PersonEntity


class PersonDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, PersonEntity)

    def read_all_by_names(self, names):
        objs = self.db.session.query(self.class_entity).filter(self.class_entity.name.in_(names)).all()
        return objs

    def read_all_by_building_room_id(self, id):
        objs = self.db.session.query(self.class_entity).filter_by(building_room_id=id).all()
        return objs

    def read_all_owned(self):
        objs = self.db.session.query(self.class_entity).filter_by(owned=True).all()
        return objs
