from ..base_dao import BaseDAO
from ..entity import ResourceEntity


class ResourceDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, ResourceEntity)

    def read_all_by_names(self, names):
        objs = self.db.session.query(self.class_entity).filter(self.class_entity.name.in_(names)).all()
        return objs

    def read_all_by_type_id(self, id):
        # obj = self.db.session.query(self.class_entity).join(ResourceTypeEntity).filter(
        #     ResourceTypeEntity.id == id).all()
        obj = self.db.session.query(self.class_entity).filter_by(resource_type_id=id).all()
        return obj

    def delete(self, id):
        obj = self.read_by_id(id)
        self.db.session.delete(obj)
        self.db.session.commit()
