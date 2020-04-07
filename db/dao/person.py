from ..base_dao import BaseDAO
from ..entity import PersonEntity


class PersonDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, PersonEntity)

    def read_all_by_names(self, names):
        objs = self.db.session.query(self.class_entity).filter(self.class_entity.name.in_(names)).all()
        return objs

    def update_by_id(self, id, **kwargs):
        obj = self.read_by_id(id)
        if obj is not None:
            obj.update(**kwargs)
            self.db.session.commit()
        return obj

    def delete(self, id):
        obj = self.read_by_id(id)
        if obj is not None:
            self.db.session.delete(obj)
            self.db.session.commit()
