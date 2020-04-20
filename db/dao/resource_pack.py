from ..base_dao import BaseDAO
from ..entity import ResourceTypeEntity, ResourcePackEntity


class ResourcePackDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db, ResourcePackEntity)

    def read_by_name(self, name):
        obj = self.db.session.query(self.class_entity).filter_by(name=name).one_or_none()
        return obj

    def read_by_type_id_and_quantity(self, type_id, quantity):
        obj = self.db.session.query(self.class_entity).filter_by(skill_type_id=type_id, quantity=quantity).one_or_none()
        return obj

    def read_by_type_name_and_quantity(self, type_name, quantity):
        obj = self.db.session.query(self.class_entity).join(ResourceTypeEntity).filter(
            ResourceTypeEntity.name == type_name, self.class_entity.quantity == quantity).one_or_none()
        return obj
