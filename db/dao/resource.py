from ..base_dao import BaseDAO
from ..entity import ResourceEntity


class ResourceDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, ResourceEntity)

    def read_all_by_names(self, names):
        objs = self.db.session.query(self.class_entity).filter(self.class_entity.name.in_(names)).all()
        return objs

    def read_all_by_type(self, name):
        # obj = self.db.session.query(self.class_entity).join(ResourceTypeEntity).filter(
        #     ResourceTypeEntity.id == id).all()
        objs = self.db.session.query(self.class_entity).filter_by(type=name).all()
        return objs

    def read_all_owned(self):
        objs = self.db.session.query(self.class_entity).filter_by(owned=True).all()
        return objs
